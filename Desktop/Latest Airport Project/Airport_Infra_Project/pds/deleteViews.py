from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.views import generic 
import datetime
 
# Create your views here.
from .models import Personal, Payroll, Bonuses, Children, Education, Eligibility, Experience, Voluntary, Learning, Otherinfo, Refferences, Other_skills, Other_recognitions, Other_membership, Post
from .forms import PersonalInfoForm, ChildrenForm, EducationForm, EligibilityForm, ExperienceForm, VoluntaryForm, LearningForm, OtherinfoForm, RefferencesForm, Other_membershipForm, Other_recognitionsForm, Other_skillsForm

@login_required
def ChildDelete(request, id):
    info = Personal.objects.filter(author=request.user).first()
    child = Children.objects.get(id=id)
    if info.id == child.child_id:
        pds  = Children.objects.get(id=id)
        pds.delete()
        return redirect('/pds/personalinfo') 
    else:
        return redirect('/pds')

@login_required
def EducationDelete(request, id):
    info = Personal.objects.filter(author=request.user).first()
    educ = Education.objects.get(id=id)
    if info.id == educ.education_id:
        pds  = Education.objects.get(id=id)
        pds.delete()
        return redirect('/pds/personalinfo')
    else:
        return redirect('/pds')

@login_required
def EligibilityDelete(request, id):
    info = Personal.objects.filter(author=request.user).first()
    elig = Eligibility.objects.get(id=id)
    if info.id == elig.eligible_id:
        pds  = Eligibility.objects.get(id=id)
        pds.delete()
        return redirect('/pds/personalinfo2')
    else:
        return redirect('/pds')

@login_required
def ExperienceDelete(request, id):
    info = Personal.objects.filter(author=request.user).first()
    exp = Experience.objects.get(id=id)
    if info.id == exp.exp_id:
        pds  = Experience.objects.get(id=id)
        pds.delete()
        return redirect('/pds/personalinfo2')
    else:
        return redirect('/pds')

@login_required
def VoluntaryDelete(request, id):
    info = Personal.objects.filter(author=request.user).first()
    vol = Voluntary.objects.get(id=id)
    if info.id == vol.voluntary_id:
        pds  = Voluntary.objects.get(id=id)
        pds.delete()
        return redirect('/pds/personalinfo3')
    else:
        return redirect('/pds')

@login_required
def LearningDelete(request, id):
    info = Personal.objects.filter(author=request.user).first()
    learn = Learning.objects.get(id=id)
    if info.id == learn.learn_id:
        pds  = Learning.objects.get(id=id)
        pds.delete()
        return redirect('/pds/personalinfo3')
    else:
        return redirect('/pds')

@login_required
def SkillsDelete(request, id):
    info = Personal.objects.filter(author=request.user).first()
    skill = Other_skills.objects.get(id=id)
    if info.id == skill.ski_id:
        pds  = Other_skills.objects.get(id=id)
        pds.delete()
        return redirect('/pds/personalinfo3')
    else:
        return redirect('/pds')

@login_required
def RecognitionsDelete(request, id):
    info = Personal.objects.filter(author=request.user).first()
    recog = Other_recognitions.objects.get(id=id)
    if info.id == recog.recog_id:
        pds  = Other_recognitions.objects.get(id=id)
        pds.delete()
        return redirect('/pds/personalinfo3')
    else:
        return redirect('/pds')

@login_required
def MembershipDelete(request, id):
    info = Personal.objects.filter(author=request.user).first()
    member = Other_membership.objects.get(id=id)
    if info.id == member.member_id:
        pds  = Other_membership.objects.get(id=id)
        pds.delete()
        return redirect('/pds/personalinfo3')
    else:
        return redirect('/pds')

@login_required
def RefferencesDelete(request, id):
    info = Personal.objects.filter(author=request.user).first()
    refer = Refferences.objects.get(id=id)
    if info.id == refer.refer_id:
        pds  = Refferences.objects.get(id=id)
        pds.delete()
        return redirect('/pds/personalinfo4')
    else:
        return redirect('/pds')

@login_required
def DeletePost(request, id):
    
    if request.user.groups.filter(name='hrmd'):
        data  = Post.objects.get(id=id)
        data.delete()
        return redirect('/pds/post')
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def PayrollDelete(request, id):
    
    if request.user.groups.filter(name='payroll'):
        data  = Payroll.objects.get(id=id)
        data.delete()
        if data.office == 'AANSOO':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/aansoo_payroll')
        elif data.office == 'ANS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/ans_payroll')
        elif data.office == 'ADMS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/adms_payroll')
        elif data.office == 'ATS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/ats_payroll')
        elif data.office == 'CATC':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/catc_payroll')
        elif data.office == 'CSIS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/csis_payroll')
        elif data.office == 'ELS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/els_payroll')
        elif data.office == 'FICG':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/ficg_payroll')
        elif data.office == 'FD':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/fmd_payroll')
        elif data.office == 'FSIS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/fsis_payroll')
        elif data.office == 'IAS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/ias_payroll')
        elif data.office == 'ODG':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/odg_payroll')
        elif data.office == 'OFSAM':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/ofsam_payroll')
        elif data.office == 'ADMIN':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Payroll.')
            return redirect('/pds/admin_payroll')
        else:
            return redirect('/pds/payroll')
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def BonusDelete(request, id):
    
    if request.user.groups.filter(name='payroll'):
        data  = Bonuses.objects.get(id=id)
        data.delete()
        if data.office == 'AANSOO':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/aansoo_payroll_nov')
        elif data.office == 'ANS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/ans_payroll_nov')
        elif data.office == 'ADMS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/adms_payroll_nov')
        elif data.office == 'ATS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/ats_payroll_nov')
        elif data.office == 'CATC':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/catc_payroll_nov')
        elif data.office == 'CSIS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/csis_payroll_nov')
        elif data.office == 'ELS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/els_payroll_nov')
        elif data.office == 'FICG':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/ficg_payroll_nov')
        elif data.office == 'FD':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/fmd_payroll_nov')
        elif data.office == 'FSIS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/fsis_payroll_nov')
        elif data.office == 'IAS':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/ias_payroll_nov')
        elif data.office == 'ODG':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/odg_payroll_nov')
        elif data.office == 'OFSAM':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/ofsam_payroll_nov')
        elif data.office == 'ADMIN':
            messages.success(request, 'Successfully deleted' + ' ... '  + str(data.first_name) + ', ' + str(data.surname) +"'" + ' Bonus Payroll.')
            return redirect('/pds/admin_payroll_nov')
        else:
            return redirect('/pds/payroll')
    else:
        return HttpResponseRedirect(reverse('pds:index'))