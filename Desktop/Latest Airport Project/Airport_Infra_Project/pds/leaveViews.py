from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib import messages
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.db.models import Q
import datetime
from datetime import date
 
# Create your views here.
from .models import Personal, Leave, SPFLeave
from .forms import PersonalInfoForm , LeaveForm, SPFLeaveForm

@login_required
def leaveCredits(request):
    pds = Personal.objects.filter(author=request.user).first()
    leave = Leave.objects.filter(leave_id=pds.id).order_by('id').last()
    spfleave = SPFLeave.objects.filter(leave_id=pds.id).first()
    context = {'leave': leave,'spfleave': spfleave, 'pds':pds}
    return render(request, 'pds/leavecredits/index.html', context)

@login_required
def leaveView(request, id):
    employee = Personal.objects.get(id=id)
    vacation = Leave.objects.filter(leave_id = id).order_by('id').last()
    leaves = Leave.objects.filter(leave_id=id).order_by('id')
    spfleave = SPFLeave.objects.filter(leave_id=id).first()
    today = datetime.date.today()
    context = {'leaves': leaves,'employee': employee,'today': today,'spfleave': spfleave, 'vacation':vacation}
    if request.user.groups.filter(name='leave'):
        return render(request, 'pds/leave/index.html', context)
    else:
        return redirect('/pds')

@login_required
def leaveCreate(request, id):
    if request.user.groups.filter(name='leave'):
        if request.method == 'POST':
            personal = Personal.objects.get(id=id)
            form = LeaveForm(request.POST)
            vacation = Leave.objects.filter(leave_id = id).order_by('-id').first()
            vacation_earned = request.POST['vacation_earned']
            vacation_wpay = request.POST['vacation_wpay']
            vacation_wopay = request.POST['vacation_wopay']
            sick_earned = request.POST['vacation_earned']
            sick_wpay = request.POST['sick_wpay']
            sick_wopay = request.POST['sick_wopay']

            if vacation:
                vacation_bal = vacation.vacation_balance
                vacation_bal = float(vacation_bal) + float(vacation_earned)
                vacation_bal = float(vacation_bal) - float(vacation_wpay)
                # vacation_bal = float(vacation_bal) - float(vacation_wopay)
                sick_bal = vacation.sick_balance
                sick_bal = float(sick_bal) + float(sick_earned)
                sick_bal = float(sick_bal) - float(sick_wpay)
                # sick_bal = float(sick_bal) - float(sick_wopay)
            else:
                vacation_bal = vacation_earned
                sick_bal = sick_earned


            
            personal = Personal.objects.get(id=id)
            instance = form.save(commit=False)
            instance.leave_id = personal.id
            instance.vacation_balance = vacation_bal
            instance.sick_balance = sick_bal
            if sick_earned != 0.000:
                instance.sick_earned = sick_earned
            instance.created_at = datetime.datetime.now()
            instance.updated_by = request.user.first_name
            instance.save()

            return redirect('/pds/leave/' + str(id))      
        else:
            employee = Personal.objects.get(id=id)
            form = LeaveForm(request.POST)
        return render(request,'pds/leave/create.html',{'form':form,'employee':employee})
    else:
        return redirect('/pds')

@login_required
def leaveUpdate(request, id):
    if request.user.groups.filter(name='leave'):
        if request.method == 'POST':
            personal = Personal.objects.get(id=id)
            edit_id = Leave.objects.get(id=id)
            form = LeaveForm(request.POST)
            vacation = Leave.objects.filter(leave_id = edit_id.leave_id).order_by('-created_at').first()
            vacation_earned = request.POST['vacation_earned']
            vacation_wpay = request.POST['vacation_wpay']
            vacation_wopay = request.POST['vacation_wopay']
            sick_earned = request.POST['sick_earned']
            sick_wpay = request.POST['sick_wpay']
            sick_wopay = request.POST['sick_wopay']

            vacation_bal = vacation.vacation_balance
            vacation_bal = float(vacation_bal) + float(vacation_earned)
            vacation_bal = float(vacation_bal) - float(vacation_wpay)
            # vacation_bal = float(vacation_bal) - float(vacation_wopay)
            sick_bal = vacation.sick_balance
            sick_bal = float(sick_bal) + float(sick_earned)
            sick_bal = float(sick_bal) - float(sick_wpay)
            # sick_bal = float(sick_bal) - float(sick_wopay)


            if vacation:
               personal = Personal.objects.get(id=id)
               instance = form.save(commit=False)
               instance.leave_id = edit_id.leave_id
               instance.id = id
               instance.vacation_balance = vacation_bal
               instance.sick_balance = sick_bal
               instance.created_at = datetime.datetime.now()
               instance.updated_by = request.user.first_name
               instance.save()

            return redirect('/pds/leave/' + str(edit_id.leave_id))      
        else:
            leave = Leave.objects.get(id=id)
            employee = Personal.objects.get(id=id)
            form = LeaveForm(request.POST)
        return render(request,'pds/leave/edit.html',{'form':form,'employee':employee,'leave':leave})
    else:
        return redirect('/pds')

@login_required
def SPFLeaveCreate(request, id):
    if request.user.groups.filter(name='leave'):

        personal = Personal.objects.get(id=id)
        spl = SPFLeave.objects.filter(leave_id = personal.id).count()

        if spl >= 1:            
            messages.success(request, 'Existing SPL and FL, go to Update')
            return redirect('/pds/leave/' + str(id))
        else:
            if request.method == 'POST':
                personal = Personal.objects.get(id=id)
                form = SPFLeaveForm(request.POST)
                instance = form.save(commit=False)
                instance.leave_id = personal.id 
                instance.updated_by = request.user.first_name
                instance.save()

                return redirect('/pds/leave/' + str(id))      
            else:
                employee = Personal.objects.get(id=id)
                form = LeaveForm(request.POST)
            return render(request,'pds/leave/spf.html',{'form':form,'employee':employee})
    else:
        return redirect('/pds')

@login_required
def SPFLeaveUpdate(request, id):
    if request.user.groups.filter(name='leave'):
        if request.method == 'POST':
            spfleave = SPFLeave.objects.filter(leave_id=id).first()
            form = SPFLeaveForm(request.POST)
            instance = form.save(commit=False)
            instance.id = spfleave.id
            instance.leave_id = spfleave.leave_id
            instance.updated_by = request.user.first_name
            instance.save()

            return redirect('/pds/leave/' + str(id))      
        else:
            spfleave = SPFLeave.objects.filter(leave_id=id).first()
            form = LeaveForm(request.POST)
        return render(request,'pds/leave/spfedit.html',{'form':form,'spfleave':spfleave})
    else:
        return redirect('/pds')

@login_required
def DeleteLeave(request, id):
    if request.user.groups.filter(name='leave'):

        leave  = Leave.objects.get(id=id)
        employee = Personal.objects.get(id=leave.leave_id)
        leave.delete()
        return redirect('/pds/leave/' + str(employee.id))
    else:
        return redirect('/pds')