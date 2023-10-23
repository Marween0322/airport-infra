from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.template import loader
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone
import datetime
from datetime import date, timedelta
# importing the necessary libraries
from .process import html_to_pdf 
from django.views import generic 
import xlwt

# Create your views here.
from .models import Personal, Payroll, Children, Education, Eligibility, Experience, Voluntary, Learning, Otherinfo, Refferences, Other_skills, Other_recognitions, Other_membership, Vaccine, Training, SalaryGrade, Position, Signatory, NotifyTraining
from .forms import PersonalInfoForm, ChildrenForm, EducationForm, EligibilityForm, ExperienceForm, VoluntaryForm, LearningForm, OtherinfoForm, RefferencesForm, Other_membershipForm, Other_recognitionsForm, Other_skillsForm,VaccineForm, CreateTrainingForm, SalaryGradeForm, PositionForm, SignatoryForm

# Account Setting
@login_required
def Settings(request):
    if request.method == 'POST':
        account = User.objects.get(id=request.user.id)
        instance = account
        instance.id = account.id
        instance.email = request.POST['email']
        instance.password = make_password(request.POST['password'])
        instance.save()
        return redirect('/pds/personalinfo')
    else:
        return render(request, 'pds/personal/settings.html')

@login_required
def VaccineShow(request):
    vaccine = Vaccine.objects.filter(vax=request.user)
    return render(request, 'pds/vaccine/index.html', {'vaccine' : vaccine})

@login_required
def VaccineCreate(request):
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES)
        if request.POST['name1']:
            dose1 = 'true'
        else:
            dose1 = 'false'
        if request.POST['name2']:
            dose2 = 'true'
        else:
            dose2 = 'false'
        if request.POST['name3']:
            dose3 = 'true'
        else:
            dose3 = 'false'
        if request.POST['name4']:
            dose4 = 'true'
        else:
            dose4 = 'false'
  
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.vax = request.user
                instance.dose1 = dose1
                instance.dose2 = dose2
                instance.dose3 = dose3
                instance.dose4 = dose4
                instance.save()
                return redirect('/pds/vaccine')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/vaccine/create.html',{'form':form})
    else:
        form = VaccineForm(request.POST)
    return render(request,'pds/vaccine/create.html',{'form':form})

@login_required
def VaccineUpdate(request, id):
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES)
        if request.FILES.get('file1'):
            file_check1 = 'True'
        else:
            file_check1 = 'False'
        if request.FILES.get('file2'):
            file_check2 = 'True'
        else:
            file_check2 = 'False'
        if request.FILES.get('file3'):
            file_check3 = 'True'
        else:
            file_check3 = 'False'
        if request.FILES.get('file4'):
            file_check4 = 'True'
        else:
            file_check4 = 'False'
        if request.POST['name1']:
            dose1 = 'true'
        else:
            dose1 = 'false'
        if request.POST['name2']:
            dose2 = 'true'
        else:
            dose2 = 'false'
        if request.POST['name3']:
            dose3 = 'true'
        else:
            dose3 = 'false'
        if request.POST['name4']:
            dose4 = 'true'
        else:
            dose4 = 'false'
  
        if form.is_valid():
                vaccine = Vaccine.objects.get(id=id)
                instance = form.save(commit=False)
                instance.vax = request.user
                instance.id = id
                instance.dose1 = dose1
                instance.dose2 = dose2
                instance.dose3 = dose3
                instance.dose4 = dose4
                if file_check1 == 'True' :
                    instance.file1 = request.FILES['file1']
                else:
                    instance.file1 = vaccine.file1
                if file_check2 == 'True' :
                    instance.file2 = request.FILES['file2']
                else:
                    instance.file2 = vaccine.file2
                if file_check3 == 'True' :
                    instance.file3 = request.FILES['file3']
                else:
                    instance.file3 = vaccine.file3
                if file_check4 == 'True' :
                    instance.file4 = request.FILES['file4']
                else:
                    instance.file4 = vaccine.file4
                instance.save()
                return redirect('/pds/vaccine')
    vaccine = Vaccine.objects.get(id=id)
    return render(request, 'pds/vaccine/edit.html', {'vaccine' : vaccine})

@login_required
def TrainingRecord(request, id):
    if request.user.groups.filter(name='training'):
        personal = Personal.objects.get(id=id)
        trainings = Learning.objects.filter(learn_id=id).order_by('-date_to')
        context = { 'personal': personal,'trainings': trainings }
        return render(request, 'pds/trainings/index.html', context)
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required
def CreateTrainingRecord(request, id):
    if request.user.groups.filter(name='training'):
        if request.method == 'POST':
            personal = Personal.objects.get(id=id)
            form = LearningForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    personal = Personal.objects.get(id=id)
                    instance = form.save(commit=False)
                    instance.training_id = personal.id
                    instance.save()
                    return redirect('/pds/hr')
                except:
                    form = LearningForm(request.POST)
                    print(form)
                    print("Invalid Form")
                    print(form.errors)
                    return render(request,'pds/trainings/create.html',{'form':form})
        else:
            form = LearningForm(request.POST)
        return render(request,'pds/trainings/create.html',{'form':form})
    else:
        return redirect('/pds')

@login_required
def EditTrainingRecord(request, id):
    if request.user.groups.filter(name='training'):
        if request.method == 'POST':
            form = LearningForm(request.POST)
            if form.is_valid():
                try:
                    training = Learning.objects.get(id=id)
                    training.remarks = request.POST['remarks']
                    training.is_approve = request.POST['is_approve']
                    training.edited_by = request.user.username
                    training.save()
                    return redirect('/pds/trainings/' + str(training.learn_id))
                except:
                    form = LearningForm(request.POST)
                    print(form)
                    print("Invalid Form")
                    print(form.errors)
                    context = {'form':form, 'training':training}
                    return render(request,'pds/trainings/edit.html', context)
        else:
            form = LearningForm(request.POST)
            training = Learning.objects.get(id=id)
            context = {'form':form, 'training':training}
        return render(request,'pds/trainings/edit.html', context)
    else:
        return redirect('/pds')

@login_required
def DeleteTrainingRecord(request, id):
    if request.user.groups.filter(name='training'):
        training  = Learning.objects.get(id=id)
        training.delete()
        return redirect('/pds/hr')
    else:
        return redirect('/pds')

@login_required
def ViewPayroll(request):
    payroll = Payroll.objects.filter(payroll_id=request.user.id).first()
    if payroll:
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = lastMonth.strftime('%B')
        year = lastMonth.strftime('%Y')
        total = payroll.pay_701 + payroll.pay_711
        return render(request, 'pds/payroll/show.html', {'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds')

@login_required
def EducationList(request, id):
    if request.user.groups.filter(name='training'):
        personal = Personal.objects.get(id=id)
        education = Education.objects.filter(education_id=id).order_by('-date_to')
        context = { 'personal': personal,'education': education }
        return render(request, 'pds/hr/education.html', context)
    else:
        return redirect('/pds')

@login_required
def EligibilityList(request, id):
    if request.user.groups.filter(name='training'):
        personal = Personal.objects.get(id=id)
        eligibility = Eligibility.objects.filter(eligible_id=id).order_by('-exam_date')
        context = { 'personal': personal,'eligibility': eligibility }
        return render(request, 'pds/hr/eligibility.html', context)
    else:
        return redirect('/pds')

@login_required
def SalaryGradeView(request):
    salary_grade = SalaryGrade.objects.all().order_by('salary_id')
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/sgtable/index.html', {'salary_grade':salary_grade})
    else:
        return redirect('/pds')
    

# Salary Grade Views
@login_required
def SalaryGradeCreate(request):
    if request.user.groups.filter(name='hrmd'):
            
        if request.method == "POST":
            form = SalaryGradeForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    instance = form.save(commit=False)
                    instance.save()
                    # Always return an HttpResponseRedirect after successfully dealing
                    # with POST data. This prevents data from being posted twice if a
                    # user hits the Back button.
                    return redirect('/pds/sg')
                except: 
                    print(form)
                    print("Invalid Form")
                    print(form.errors)
                    return render(request,'pds/sgtable/create.html',{'form':form})
        
        if request.user.groups.filter(name='hrmd'):
            form = SalaryGradeForm(request.POST)
            return render(request,'pds/sgtable/create.html',{'form':form})
        else:
            return HttpResponseRedirect(reverse('pds:index'))
    else:
        return redirect('/pds')

@login_required
def SalaryGradeEdit(request, id):
    data = SalaryGrade.objects.get(id=id)

    if request.user.groups.filter(name='hrmd'):
        return render(request,'pds/sgtable/edit.html', {'data':data})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def SalaryGradeUpdate(request, id):
    if request.user.groups.filter(name='hrmd'):    
        if request.POST:
            form = SalaryGradeForm(request.POST)
            if form.is_valid():
                data = SalaryGrade.objects.get(id=id)
                instance = form.save(commit=False)
                instance.id = data.id
                instance.salary_id = data.salary_id
                instance.updated_by = request.user.username
                instance.save()
                return redirect('/pds/sg')
            return render(request,'pds/sgtable/edit.html', {'data':data})
        return redirect('/pds/sgtable')
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def PositionView(request):
    data = Position.objects.all().order_by('id')
    if request.user.groups.filter(name='hrmd'):               
        return render(request, 'pds/position/index.html', {'data':data})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

# Position Create
@login_required
def PositionCreate(request):
    if request.user.groups.filter(name='hrmd'):       
       
        if request.method == "POST":
            form = PositionForm(request.POST)
            if form.is_valid():
                try:
                    data = Position.objects.all().last()
                    position_last = int(data.position_id) + 1

                    form.save()
                    instance = form.save(commit=False)
                    instance.position_id = position_last
                    instance.save()
                    # Always return an HttpResponseRedirect after successfully dealing
                    # with POST data. This prevents data from being posted twice if a
                    # user hits the Back button.
                    return redirect('/pds/position')
                except: 
                    print(form)
                    print("Invalid Form")
                    print(form.errors)
                    return render(request,'pds/position/create.html',{'form':form})
        if request.user.groups.filter(name='hrmd'):        
                form = PositionForm(request.POST)
                return render(request,'pds/position/create.html',{'form':form})
        else:
            return HttpResponseRedirect(reverse('pds:index'))
    else:
        return redirect('/pds') 
    

@login_required
def PositionEdit(request, id):
    data = Position.objects.get(id=id)

    if request.user.groups.filter(name='hrmd'):
        return render(request,'pds/position/edit.html', {'data':data})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def PositionUpdate(request, id):
    if request.user.groups.filter(name='hrmd'):
        
        if request.POST:
            form = PositionForm(request.POST)
            if form.is_valid():
                data = Position.objects.get(id=id)
                instance = form.save(commit=False)
                instance.id = data.id
                instance.position_id = data.position_id
                instance.updated_by = request.user.username
                instance.save()
                return redirect('/pds/position')
            return render(request,'pds/position/edit.html', {'data':data})
        return redirect('/pds/position')
    else:
        return redirect('/pds')

@login_required
def SignatoryView(request):
    data = Signatory.objects.all()

    if request.user.groups.filter(name='hrmd'):        
            return render(request, 'pds/signatory/index.html', {'data':data})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def SignatoryEdit(request, id):
    data = Signatory.objects.get(id=id)

    if request.user.groups.filter(name='hrmd'):
        return render(request,'pds/signatory/edit.html', {'data':data})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def SignatoryUpdate(request, id):
    if request.user.groups.filter(name='hrmd'):
        
        if request.POST:
            form = SignatoryForm(request.POST)
            if form.is_valid():
                data = Signatory.objects.get(id=id)
                instance = form.save(commit=False)
                instance.id = data.id
                instance.updated_by = request.user.username
                instance.save()
                return redirect('/pds/sign')
            return render(request,'pds/signatory/edit.html', {'data':data})
        return redirect('/pds/signatory')
    else:
        return redirect('/pds')


@login_required
def TrainingRecordNotif(request):

    data = NotifyTraining.objects.all().order_by('id')

    if request.user.groups.filter(name='training'):
        return render(request, 'pds/trainings/notify.html', {'data':data})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')


# Privacy Notice
def PrivacyPage(request):

    return render(request,'privacy.html')


# Privacy Notice
def HelpPage(request):

    return render(request,'help.html')

# Frequently Answered Questions
def FAQPage(request):

    return render(request,'faq.html')