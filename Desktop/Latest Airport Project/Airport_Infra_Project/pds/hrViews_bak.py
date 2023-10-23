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
import xlwt 
import datetime 
 
# Create your views here.
from .models import Personal, Payroll, Children, Education, Eligibility, Experience, Voluntary, Learning, Otherinfo, Refferences, Other_skills, Other_recognitions, Other_membership, Vaccine, SalaryGrade, Position
from .forms import PersonalInfoForm, VaccineForm, PayrollForm, UserForm


# Admin Views 
@login_required
def Dashboard(request):
    # Assignment
    central = Personal.objects.filter(assignment__iexact='Central Office').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A1 = Personal.objects.filter(assignment__iexact='Area 01').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A2 = Personal.objects.filter(assignment__iexact='Area 02').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A3 = Personal.objects.filter(assignment__iexact='Area 03').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A4 = Personal.objects.filter(assignment__iexact='Area 04').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A5 = Personal.objects.filter(assignment__iexact='Area 05').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A6 = Personal.objects.filter(assignment__iexact='Area 06').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A7 = Personal.objects.filter(assignment__iexact='Area 07').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A8 = Personal.objects.filter(assignment__iexact='Area 08').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A9 = Personal.objects.filter(assignment__iexact='Area 09').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A10 = Personal.objects.filter(assignment__iexact='Area 10').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A11 = Personal.objects.filter(assignment__iexact='Area 11').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    A12 = Personal.objects.filter(assignment__iexact='Area 12').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()

    total = int(central) + int(A1) + int(A2) + int(A3) + int(A4) + int(A5) + int(A6) + int(A7) + int(A8) + int(A9) + int(A10) + int(A11) + int(A12)

    startTotal = int(total) - 200

    male = Personal.objects.filter(sex__iexact='Male').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    female = Personal.objects.filter(sex__iexact='female').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    married = Personal.objects.filter(civil_status__iexact='Married').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    single = Personal.objects.filter(civil_status__iexact='Single').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    widowed = Personal.objects.filter(civil_status__iexact='Widowed').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    annulled = Personal.objects.filter(civil_status__iexact='Annulled Mariage').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    permanent = Personal.objects.filter(emp_type__iexact='Permanent').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    joborder = Personal.objects.filter(emp_type__iexact='Job Order').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    outsource = Personal.objects.filter(emp_type__iexact='Outsourced').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    consultant = Personal.objects.filter(emp_type__iexact='Contract of Service').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    coterm = Personal.objects.filter(emp_type__iexact='Co-Terminus').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    first_dose = Vaccine.objects.filter(dose1__iexact='true').count()
    second_dose = Vaccine.objects.filter(dose2__iexact='true').count()
    booster = Vaccine.objects.filter(dose3__iexact='true').count()
    booster2 = Vaccine.objects.filter(dose4__iexact='true').count()
    info_count = Otherinfo.objects.all().count()
    soloparent = Otherinfo.objects.filter(soloparent__iexact='Yes').count()
    parent = total - soloparent
    disability = Otherinfo.objects.filter(disability__iexact='Yes').count()
    
    pds_count = Personal.objects.exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()

    # Assignment Jo Permanent
    perma_central = Personal.objects.filter(Q(assignment__iexact='Central Office')).filter(Q(emp_type="Permanent")| Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A1 = Personal.objects.filter(Q(assignment__iexact='Area 01')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A2 = Personal.objects.filter(Q(assignment__iexact='Area 02')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A3 = Personal.objects.filter(Q(assignment__iexact='Area 03')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A4 = Personal.objects.filter(Q(assignment__iexact='Area 04')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A5 = Personal.objects.filter(Q(assignment__iexact='Area 05')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A6 = Personal.objects.filter(Q(assignment__iexact='Area 06')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A7 = Personal.objects.filter(Q(assignment__iexact='Area 07')).filter(Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A8 = Personal.objects.filter(Q(assignment__iexact='Area 08')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A9 = Personal.objects.filter(Q(assignment__iexact='Area 09')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A10 = Personal.objects.filter(Q(assignment__iexact='Area 10')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A11 = Personal.objects.filter(Q(assignment__iexact='Area 11')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    perma_A12 = Personal.objects.filter(Q(assignment__iexact='Area 12')).filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_central = Personal.objects.filter(Q(assignment__iexact='Central Office')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A1 = Personal.objects.filter(Q(assignment__iexact='Area 01')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")   ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A2 = Personal.objects.filter(Q(assignment__iexact='Area 02')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A3 = Personal.objects.filter(Q(assignment__iexact='Area 03')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A4 = Personal.objects.filter(Q(assignment__iexact='Area 04')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A5 = Personal.objects.filter(Q(assignment__iexact='Area 05')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A6 = Personal.objects.filter(Q(assignment__iexact='Area 06')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A7 = Personal.objects.filter(Q(assignment__iexact='Area 07')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A8 = Personal.objects.filter(Q(assignment__iexact='Area 08')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A9 = Personal.objects.filter(Q(assignment__iexact='Area 09')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A10 = Personal.objects.filter(Q(assignment__iexact='Area 10')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A11 = Personal.objects.filter(Q(assignment__iexact='Area 11')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    jo_A12 = Personal.objects.filter(Q(assignment__iexact='Area 12')).filter( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="LSERV") | Q(emp_type="Outsourced")  ).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()

    senior = Personal.objects.filter(gcg_sdd="Senior Management").exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    middle = Personal.objects.filter(gcg_sdd="Middle Management").exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    visor = Personal.objects.filter(gcg_sdd="Professional & Supervisory").exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    genstaff = Personal.objects.filter(gcg_sdd="Clerical & General Staff").exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    

    good = total - disability
    if info_count == 0:
        soloparentP = 0
    else:
        soloparentP = round((soloparent/total) * 100, 2)
    if info_count == 0:
        disabilityP = 0
    else:
        disabilityP = round((disability/total) * 100, 2)
    if pds_count == 0:
        maleP = 0
        femaleP = 0
        marriedP = 0
        singleP = 0
        widowedP = 0
        annulledP = 0
        permanentP = 0
        joborderP = 0
        outsourceP = 0
        consultantP = 0
        cotermP = 0
    else:
        maleP = round((male/total) * 100, 2)
        femaleP = round((female/total) * 100, 2)
        marriedP = round((married/total) * 100, 2)
        singleP = round((single/total) * 100, 2)
        widowedP = round((widowed/total) * 100, 2)
        annulledP = round((annulled/total) * 100, 2)
        permanentP = round((permanent/total) * 100, 2)
        joborderP = round((joborder/total) * 100, 2)
        outsourceP = round((outsource/total) * 100, 2)
        consultantP = round((consultant/total) * 100, 2)
        cotermP = round((coterm/total) * 100, 2)

    

    datetoday = datetime.datetime.now()
    today = datetoday.strftime('%B %d, %Y')

    context = {'total':total, 'startTotal': startTotal,'male':male, 'female':female, 'maleP':maleP, 'marriedP':marriedP, 'singleP':singleP, 'widowedP':widowedP, 'annulledP':annulledP, 'femaleP':femaleP, 'married':married, 'single':single, 'widowed':widowed, 'annulled':annulled, 'permanent':permanent, 'joborder':joborder, 'outsource':outsource, 'consultant':consultant, 'coterm':coterm, 'first_dose':first_dose, 'second_dose':second_dose, 'booster':booster , 'booster2':booster2, 'permanentP':permanentP, 'joborderP':joborderP, 'outsourceP':outsourceP, 'consultantP':consultantP, 'cotermP':cotermP, 'disability':disability, 'soloparent':soloparent , 'parent':parent, 'good':good, 'disabilityP':disabilityP, 'soloparentP':soloparentP, 'central':central, 'A1':A1, 'A2':A2, 'A3':A3, 'A4':A4, 'A5':A5, 'A6':A6, 'A7':A7, 'A8':A8, 'A9':A9, 'A10':A10, 'A11':A11 , 'A12':A12 , 'today': today, 'perma_central' : perma_central , 'perma_A1' : perma_A1 ,'perma_A2' : perma_A2 ,'perma_A3' : perma_A3 ,'perma_A4' : perma_A4 ,'perma_A5' : perma_A5 ,'perma_A6' : perma_A6 ,'perma_A7' : perma_A7 ,'perma_A8' : perma_A8 ,'perma_A9' : perma_A9 ,'perma_A10' : perma_A10 ,'perma_A11' : perma_A11 ,'perma_A12' : perma_A12, 'jo_central' : jo_central , 'jo_A1' : jo_A1 ,'jo_A2' : jo_A2 ,'jo_A3' : jo_A3 ,'jo_A4' : jo_A4 ,'jo_A5' : jo_A5 ,'jo_A6' : jo_A6 ,'jo_A7' : jo_A7 ,'jo_A8' : jo_A8 ,'jo_A9' : jo_A9 ,'jo_A10' : jo_A10 ,'jo_A11' : jo_A11 ,'jo_A12' : jo_A12 ,'senior' : senior ,'middle' : middle ,'visor' : visor ,'genstaff' : genstaff } 


    if request.user.is_staff:
        return render(request, 'pds/hr/index.html', context)
    else:
        return redirect('/pds')


# Permanent List
@login_required
def Permanent(request):
    perma_list = Personal.objects.filter( Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY")).order_by('surname').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") )[:300]
    
    # perma_list.exclude(status="For Approval")[:100]
    permanent = Personal.objects.filter(emp_type__iexact='Permanent').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    context = {'perma_list': perma_list, 'permanent': permanent}
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/permanent.html', context)
    else:
        return redirect('/pds')

# Edit Permanent Item Edit
@login_required
def PermanentItemEdit(request, id):
    pds = Personal.objects.get(id=id)
   
    if request.user.groups.filter(name='hrmd'):
        return render(request,'pds/item/edit.html', {'pds':pds})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def PermanentItemUpdate(request, id):
    if request.user.groups.filter(name='hrmd'):
        if request.POST:
            pds = Personal.objects.get(id=id)
            form = PersonalInfoForm(request.POST, instance = pds)
            # return HttpResponse(pds.author)
            if form.is_valid():

                pds = Personal.objects.get(id=id)
                pds.item = request.POST['item']

                if request.POST['salary_id'] == 'None':
                    pass
                else:
                    sg = SalaryGrade.objects.get(salary_id=request.POST['salary_id'])
                    annual = int(sg.rate) * 12 
                if request.POST['salary_id'] == 'None':
                    pass
                else:
                    pds.rate = sg.rate
                    pds.salary_id = request.POST['salary_id']
                    pds.salary_grade = sg.grade
                    pds.step = sg.step
                    pds.actual_annual = annual            
                pds.rate_perday = request.POST['rate_perday']
                pds.last_promotion = request.POST['last_promotion']
                pds.original_appointment = request.POST['original_appointment']
                pds.save()
                if pds.emp_type == 'Outsourced' or pds.emp_type == 'Job Order' or pds.emp_type == 'Contract of Service':
                    return redirect('/pds/os')
                if pds.emp_type == 'Permanent' or pds.emp_type == 'Presidential Appointee' or pds.emp_type == 'Co-terminous'or pds.emp_type == 'Temporary':
                    return redirect('/pds/permanent')
            context = {'pds':pds,'form':form }
            return render(request,'pds/item/edit.html', context)
        return redirect('/pds/permanent')
    return redirect('/pds/permanent')

# Edit Data
@login_required
def DataEdit(request, id):
    pds = Personal.objects.get(id=id)
   
    if request.user.groups.filter(name='hrmd'):
        return render(request,'pds/status/data.html', {'pds':pds})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def DataUpdate(request, id):
    if request.user.groups.filter(name='hrmd'):
        if request.POST:
            pds = Personal.objects.get(id=id)
            form = PersonalInfoForm(request.POST, instance = pds)
            # return HttpResponse(pds.author)
            if form.is_valid():
                pds = Personal.objects.get(id=id)
                pds.pagibig = request.POST['pagibig']
                pds.philhealth = request.POST['philhealth']
                pds.gsis = request.POST['gsis']
                pds.sss = request.POST['sss']
                pds.umid = request.POST['umid']
                pds.tin = request.POST['tin']
                pds.surname = request.POST['surname']
                pds.first_name = request.POST['first_name']
                pds.middle_name = request.POST['middle_name']
                pds.ext_name = request.POST['ext_name']
                pds.birth_date = request.POST['birth_date']
                pds.birth_place = request.POST['birth_place']
                pds.sex = request.POST['sex']
                pds.civil_status = request.POST['civil_status']
                pds.height = request.POST['height']
                pds.weight = request.POST['weight']
                pds.blood_type = request.POST['blood_type']
                pds.emp_number = request.POST['emp_number']
                pds.citizenship = request.POST['citizenship']
                pds.citizen_detail = request.POST['citizen_detail']
                pds.res_numstreet = request.POST['res_numstreet']
                pds.res_region = request.POST['res_region']
                pds.res_brgy = request.POST['res_brgy']
                pds.res_city = request.POST['res_city']
                pds.res_province = request.POST['res_province']
                pds.res_zip = request.POST['res_zip']
                pds.perma_numstreet = request.POST['perma_numstreet']
                pds.perma_region = request.POST['perma_region']
                pds.perma_brgy = request.POST['perma_brgy']
                pds.perma_city = request.POST['perma_city']
                pds.perma_province = request.POST['perma_province']
                pds.perma_zip = request.POST['perma_zip']
                pds.telephone = request.POST['telephone']
                pds.mobile = request.POST['mobile']
                pds.email = request.POST['email']
                pds.spouse_surname = request.POST['spouse_surname']
                pds.spouse_name = request.POST['spouse_name']
                pds.spouse_middle = request.POST['spouse_middle']
                pds.spouse_ext = request.POST['spouse_ext']
                pds.spouse_occupation = request.POST['spouse_occupation']
                pds.emb_biz = request.POST['emb_biz']
                pds.emb_biz_add = request.POST['emb_biz_add']
                pds.phone = request.POST['phone']
                pds.dad_surname = request.POST['dad_surname']
                pds.dad_name = request.POST['dad_name']
                pds.dad_middle = request.POST['dad_middle']
                pds.dad_ext = request.POST['dad_ext']
                pds.mom_surname = request.POST['mom_surname']
                pds.mom_name = request.POST['mom_name']
                pds.mom_middle = request.POST['mom_middle']
                pds.edited_by = request.user.username
                pds.save()
                return redirect('/pds/permanent')
            context = {'pds':pds,'form':form }
            return render(request,'pds/status/data.html', context)
        return redirect('/pds/permanent')
    return redirect('/pds/permanent')

# Edit Status
@login_required
def StatusEdit(request, id):
    pds = Personal.objects.get(id=id)
   
    if request.user.groups.filter(name='hrmd'):
        return render(request,'pds/status/edit.html', {'pds':pds})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def StatusUpdate(request, id):
    if request.user.groups.filter(name='hrmd'):
        if request.POST:
            pds = Personal.objects.get(id=id)
            form = PersonalInfoForm(request.POST, instance = pds)
            # return HttpResponse(pds.author)
            if form.is_valid():
                pds = Personal.objects.get(id=id)
                pds.emp_type = request.POST['emp_type']
                if (request.POST['emp_type'] == 'Separated'):
                    pds.mode_separate = request.POST['mode_separate']
                    pds.separate_date = request.POST['separate_date']
                pds.save()
                return redirect('/pds/permanent')
            context = {'pds':pds,'form':form }
            return render(request,'pds/status/edit.html', context)
        return redirect('/pds/permanent')
    return redirect('/pds/permanent')

# Edit Status
@login_required
def PositionEdit(request, id):
    pds = Personal.objects.get(id=id)
   
    if request.user.groups.filter(name='hrmd'):
        return render(request,'pds/position/edit.html', {'pds':pds})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def PositionUpdate(request, id):
    if request.user.groups.filter(name='hrmd'):
        if request.POST:
            pds = Personal.objects.get(id=id)
            form = PersonalInfoForm(request.POST, instance = pds)
            # return HttpResponse(pds.author)
            if form.is_valid():
                position = Position.objects.get(position_id=request.POST['position_title'])

                pds = Personal.objects.get(id=id)
                pds.position_title = position.name
                pds.tech_none = position.classification
                pds.gcg_sdd = position.gcg
                pds.position_id = position.position_id
                pds.dotr_level = position.dotr
                pds.updated_by = request.user.username
                pds.save()
                return redirect('/pds/permanent')
            context = {'pds':pds,'form':form }
            return render(request,'pds/position/edit.html', context)
        return redirect('/pds/permanent')
    return redirect('/pds/permanent')

@login_required
def OfficeEdit(request, id):
    pds = Personal.objects.get(id=id)
   
    if request.user.groups.filter(name='hrmd'):
        return render(request,'pds/office/edit.html', {'pds':pds})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def OfficeUpdate(request, id):
    if request.user.groups.filter(name='hrmd'):
        if request.POST:
            pds = Personal.objects.get(id=id)
            form = PersonalInfoForm(request.POST, instance = pds)
            # return HttpResponse(pds.author)
            if form.is_valid():
                pds = Personal.objects.get(id=id)
                pds.office = request.POST['office']
                pds.assignment = request.POST['assignment']
                pds.service = request.POST['service']
                pds.save()
                return redirect('/pds/permanent')
            context = {'pds':pds,'form':form }
            return render(request,'pds/office/edit.html', context)
        return redirect('/pds/permanent')
    return redirect('/pds/permanent')

@login_required
def SearchPermanent(request):
    value = request.POST['search']
    perma_list = Personal.objects.filter(Q(surname__icontains=value)|Q(first_name__icontains=value)).order_by('surname').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") )
    context = {'perma_list': perma_list, 'value' : value}
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/permanent.html', context)
    else:
        return redirect('/pds')

# JO List
@login_required
def JO(request):

    jo_list = Personal.objects.filter(emp_type="Job Order").order_by('surname').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") )
    jo = Personal.objects.filter(emp_type__iexact='Job Order').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    context = {'jo_list': jo_list, 'jo': jo}
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/jo.html', context)
    else:
        return redirect('/pds')

# outsource List
@login_required
def Outsourced(request):

    outsource_list = Personal.objects.filter(( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="Outsourced") | Q(emp_type="LSERV")  )).order_by('surname').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") )[:200]
    outsource = Personal.objects.filter(( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="Outsourced") | Q(emp_type="LSERV")  )).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    context = {'outsource_list': outsource_list, 'outsource': outsource}
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/outsource.html', context)
    else:
        return redirect('/pds')

# COTERM List
@login_required
def Coterm(request):

    coterm_list = Personal.objects.filter(Q(emp_type="Co-Terminus") | Q(emp_type="Presidential Appointee" ) | Q(emp_type="TEMPORARY")).order_by('surname').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") )
    coterm = Personal.objects.filter(emp_type__iexact='Co-Terminus').exclude(emp_type="Separated").count()
    context = {'coterm_list': coterm_list, 'coterm': coterm}
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/coterm.html', context)
    else:
        return redirect('/pds')

# Consultant List
@login_required
def Consultant(request):

    consultant_list = Personal.objects.filter(emp_type="Contract of Service").order_by('surname').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") )
    consultant = Personal.objects.filter(emp_type__iexact='Contract of Service').exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).count()
    context = {'consultant_list': consultant_list, 'consultant': consultant}
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/consultant.html', context)
    else:
        return redirect('/pds')

# Separated List
@login_required
def Separated(request):

    separate_list = Personal.objects.filter(Q(emp_type="Separated") | Q(emp_type__isnull=True)).order_by('surname').exclude(status="For Approval")
    separate = Personal.objects.filter(emp_type__iexact='Separated').count()
    context = {'separate_list': separate_list, 'separate': separate}
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/separate.html', context)
    else:
        return redirect('/pds')

# Separated List
@login_required
def ForApproval(request):

    for_approval_list = Personal.objects.filter(Q(status="For Approval") | Q(status="Disapproved")).order_by('id')
    approval = Personal.objects.filter(status="For Approval").count()
    context = {'for_approval_list': for_approval_list, 'approval': approval}
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/forapproval.html', context)
    else:
        return redirect('/pds')

# Edit For Approval
@login_required
def ForApprovalEdit(request, id):
    pds = Personal.objects.get(id=id)
   
    if request.user.groups.filter(name='hrmd'):
        return render(request,'pds/approval/edit.html', {'pds':pds})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def ForApprovalUpdate(request, id):
    if request.user.groups.filter(name='hrmd'):
        if request.POST:
            pds = Personal.objects.get(id=id)
            form = PersonalInfoForm(request.POST, instance = pds)
            # return HttpResponse(pds.author)
            if form.is_valid():            
                pds = Personal.objects.get(id=id) 
                position = Position.objects.get(position_id=request.POST['position_title'])

                if request.POST['salary_id'] == 'None':
                    pass
                else:
                    sg = SalaryGrade.objects.get(salary_id=request.POST['salary_id'])
                    annual = int(sg.rate) * 12 

                if request.POST['original_appointment'] == '':
                    pass
                else:                
                    pds.original_appointment = request.POST['original_appointment']  
                if request.POST['last_promotion'] == '':
                    pass
                else:
                    pds.last_promotion = request.POST['last_promotion']

                if request.POST['rate_perday'] == '':
                    pass
                else:                
                    pds.rate_perday = request.POST['rate_perday']  

                if request.POST['emp_number'] == '':
                    pass
                else:                
                    pds.emp_number = request.POST['emp_number']   

                if request.POST['item'] == '':
                    pass
                else:                     
                    pds.item = request.POST['item']

                if request.POST['service'] == '':
                    pass
                else:                     
                    pds.service = request.POST['service']

                if request.POST['assignment'] == '':
                    pass
                else:                     
                    pds.assignment = request.POST['assignment']

                if request.POST['office'] == '':
                    pass
                else:                     
                    pds.office = request.POST['office']

                pds.status = request.POST['approval'] 
                pds.emp_type = request.POST['emp_type']  
                pds.position_title = position.name
                pds.position_id = position.position_id
                pds.tech_none = position.classification
                pds.gcg_sdd = position.gcg
                pds.dotr_level = position.dotr
                if request.POST['salary_id'] == 'None':
                    pass
                else:
                    pds.rate = sg.rate
                    pds.salary_id = request.POST['salary_id']
                    pds.salary_grade = sg.grade
                    pds.step = sg.step
                    pds.actual_annual = annual
                pds.save()            
                messages.success(request, 'You have updated to' + str(pds.status) + ' ... '  + str(pds.first_name) + ', ' + str(pds.surname) +"'" + ' Account.')
                return redirect('/pds/for-approval')
            context = {'pds':pds,'form':form }
            return render(request,'pds/approval/edit.html', context)
        return redirect('/pds/permanent')
    return redirect('/pds/permanent')

@login_required
def VaccineAdminShow(request):
    vaccine = Vaccine.objects.all().order_by('vax')[:20]
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/vax.html', {'vaccine' : vaccine})
    else:
        return redirect('/pds')

@login_required
def VaccineAdminDisplay(request):
    # vaccine = Vaccine.objects.get(id=id)
    value = request.POST['search']

    vaccine = Vaccine.objects.filter(vax__last_name__icontains= value)
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/vax_show.html', {'vaccine' : vaccine})
    else:
        return redirect('/pds')


@login_required
def PDS1(request, id):
    pds = Personal.objects.filter(id=id).first()
    children = Children.objects.filter(child_id=pds.id).order_by('-birth_date')
    childs = Children.objects.filter(child_id=pds.id).count()
    education = Education.objects.filter(education_id=pds.id).order_by('date_from')
    educs = Education.objects.filter(education_id=pds.id).count()
    context = {'pds': pds, 'children': children, 'childs' : childs,'educs' : educs, 'education': education }
    
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/pds.html', context)
    else:
        return redirect('/pds')


# Filter Views 
@login_required
def PermanentFilter(request):
    Filter = "True"
    emp = request.POST['emp_type']
    sex = request.POST['sex']
    civil_status = request.POST['civil_status']
    assignment = request.POST['assignment']
    office = request.POST['office']
    service = request.POST['service']


    perma_list_count = Personal.objects.all().exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") )

    if sex:
            perma_list_count = perma_list_count.filter(sex = sex)
    if civil_status:
            perma_list_count = perma_list_count.filter(civil_status = civil_status)
    if assignment:
            perma_list_count = perma_list_count.filter(assignment = assignment)
    if office:
            perma_list_count = perma_list_count.filter(office = office)
    if service:
            perma_list_count = perma_list_count.filter(service = service)
    if emp:
            perma_list_count = perma_list_count.filter(emp_type = emp).count()
    else:
            perma_list_count = perma_list_count.filter((Q(emp_type="Permanent") | Q(emp_type="Co-Terminus") | Q(emp_type="PRESIDENTIAL APPOINTEE") | Q(emp_type="TEMPORARY"))).order_by('surname').count()


    perma_list = Personal.objects.all().exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).order_by('surname')
    if sex:
            perma_list = perma_list.filter(sex = sex) 
    if civil_status:
            perma_list = perma_list.filter(civil_status__icontains = civil_status)
    if assignment:
            perma_list = perma_list.filter(assignment = assignment)
    if office:
            perma_list = perma_list.filter(office = office)
    if service:
            perma_list = perma_list.filter(service = service)
    if emp :
            perma_list = perma_list.filter(emp_type = emp)
    else:
            perma_list = perma_list.filter((Q(emp_type="Permanent") | Q(emp_type="Co-terminous") | Q(emp_type="Presidential Appointee") | Q(emp_type="Temporary")))

    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/permanent.html', {'Filter': Filter, 'perma_list': perma_list, 'perma_list_count': perma_list_count , 'sex': sex , 'civil_status': civil_status , 'assignment': assignment})
    else:
        return redirect('/pds')


@login_required
def JOFilter(request):
    Filter = "True"
    sex = request.POST['sex']
    civil_status = request.POST['civil_status']
    assignment = request.POST['assignment']
    office = request.POST['office']
    service = request.POST['service']


    jo_list_count = Personal.objects.all()
    
    if sex:
            jo_list_count = jo_list_count.filter(sex = sex)
    if civil_status:
            jo_list_count = jo_list_count.filter(civil_status = civil_status)
    if assignment:
            jo_list_count = jo_list_count.filter(assignment = assignment)
    if office:
            jo_list_count = jo_list_count.filter(office = office)
    if service:
            jo_list_count = jo_list_count.filter(service = service)

    jo_list_count = jo_list_count.filter(emp_type="Job Order").order_by('surname').count()


    jo_list = Personal.objects.all()
    if sex:
            jo_list = jo_list.filter(sex = sex)
    if civil_status:
            jo_list = jo_list.filter(civil_status__icontains = civil_status)
    if assignment:
            jo_list = jo_list.filter(assignment = assignment)
    if service:
            jo_list = jo_list.filter(service = service)

    jo_list = jo_list.filter(emp_type="Job Order").order_by('surname')


    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/jo.html', {'Filter': Filter, 'jo_list': jo_list, 'jo_list_count': jo_list_count , 'sex': sex , 'civil_status': civil_status , 'assignment': assignment})
    else:
        return redirect('/pds')


@login_required
def OutsourcedFilter(request):
    Filter = "True"    
    emp = request.POST['emp_type']
    sex = request.POST['sex']
    civil_status = request.POST['civil_status']
    assignment = request.POST['assignment']
    office = request.POST['office']
    service = request.POST['service']


    outsource_list_count = Personal.objects.all().exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") )

    
    
    if sex:
            outsource_list_count = outsource_list_count.filter(sex = sex)
    if civil_status:
            outsource_list_count = outsource_list_count.filter(civil_status__icontains = civil_status)
    if assignment:
            outsource_list_count = outsource_list_count.filter(assignment = assignment)
    if office:
            outsource_list_count = outsource_list_count.filter(office = office)
    if service:
            outsource_list_count = outsource_list_count.filter(service = service)

    if emp:
            outsource_list_count = outsource_list_count.filter(emp_type = emp).order_by('surname').count()
    else:
            outsource_list_count = outsource_list_count.filter(( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="Outsourced") | Q(emp_type="LSERV")  )).count()


    outsource_list = Personal.objects.all().exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") )

    if emp:
            outsource_list = outsource_list.filter(emp_type = emp)
    if sex:
            outsource_list = outsource_list.filter(sex = sex)
    if civil_status:
            outsource_list = outsource_list.filter(civil_status__icontains = civil_status)
    if assignment:
            outsource_list = outsource_list.filter(assignment = assignment)
    if office:
            outsource_list = outsource_list.filter(office = office)
    if service:
            outsource_list = outsource_list.filter(service = service)

    if emp:
            outsource_list = outsource_list.filter(emp_type = emp).order_by('surname')
    else:
            outsource_list = outsource_list.filter(( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="Outsourced") | Q(emp_type="LSERV")  ))


    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/outsource.html', {'Filter': Filter, 'outsource_list': outsource_list, 'outsource_list_count': outsource_list_count , 'sex': sex , 'civil_status': civil_status , 'assignment': assignment})
    else:
        return redirect('/pds')

@login_required
def CotermFilter(request):
    Filter = "True"
    sex = request.POST['sex']
    civil_status = request.POST['civil_status']
    assignment = request.POST['assignment']
    office = request.POST['office']
    service = request.POST['service']


    coterm_list_count = Personal.objects.all()
    
    if sex:
            coterm_list_count = coterm_list_count.filter(sex = sex)
    if civil_status:
            coterm_list_count = coterm_list_count.filter(civil_status__icontains = civil_status)
    if assignment:
            coterm_list_count = coterm_list_count.filter(assignment = assignment)
    if office:
            coterm_list_count = coterm_list_count.filter(office = office)
    if service:
            coterm_list_count = coterm_list_count.filter(service = service)

    coterm_list_count = coterm_list_count.filter(Q(emp_type="Co-Terminus") | Q(emp_type="Presidential Appointee")).order_by('surname').count()


    coterm_list = Personal.objects.all()
    if sex:
            coterm_list = coterm_list.filter(sex = sex)
    if civil_status:
            coterm_list = coterm_list.filter(civil_status__icontains = civil_status)
    if assignment:
            coterm_list = coterm_list.filter(assignment = assignment)
    if office:
            coterm_list = coterm_list.filter(office = office)
    if service:
            coterm_list = coterm_list.filter(service = service)

    coterm_list = coterm_list.filter(Q(emp_type="Co-Terminus") | Q(emp_type="Presidential Appointee")).order_by('surname')


    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/coterm.html', {'Filter': Filter, 'coterm_list': coterm_list, 'coterm_list_count': coterm_list_count , 'sex': sex , 'civil_status': civil_status , 'assignment': assignment})
    else:
        return redirect('/pds')

@login_required
def ConsultantFilter(request):
    Filter = "True"
    sex = request.POST['sex']
    civil_status = request.POST['civil_status']
    assignment = request.POST['assignment']
    office = request.POST['office']
    service = request.POST['service']


    consultant_list_count = Personal.objects.all()
    
    if sex:
            consultant_list_count = consultant_list_count.filter(sex = sex)
    if civil_status:
            consultant_list_count = consultant_list_count.filter(civil_status__icontains = civil_status)
    if assignment:
            consultant_list_count = consultant_list_count.filter(assignment = assignment)
    if office:
            consultant_list_count = consultant_list_count.filter(office = office)
    if service:
            consultant_list_count = consultant_list_count.filter(service = service)

    consultant_list_count = consultant_list_count.filter(emp_type="Contract of Service").order_by('surname').count()


    consultant_list = Personal.objects.all()
    if sex:
            consultant_list = consultant_list.filter(sex = sex)
    if civil_status:
            consultant_list = consultant_list.filter(civil_status__icontains = civil_status)
    if assignment:
            consultant_list = consultant_list.filter(assignment = assignment)
    if office:
            consultant_list = consultant_list.filter(office = office)
    if service:
            consultant_list = consultant_list.filter(service = service)

    consultant_list = consultant_list.filter(emp_type="Contract of Service").order_by('surname')


    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/consultant.html', {'Filter': Filter, 'consultant_list': consultant_list, 'consultant_list_count': consultant_list_count , 'sex': sex , 'civil_status': civil_status , 'assignment': assignment})
    else:
        return redirect('/pds')


@login_required
def SEFilter(request):
    Filter = "True"
    sex = request.POST['sex']
    civil_status = request.POST['civil_status']
    assignment = request.POST['assignment']
    office = request.POST['office']
    service = request.POST['service']


    separate_list_count = Personal.objects.all()
    
    if sex:
            separate_list_count = separate_list_count.filter(sex = sex)
    if civil_status:
            separate_list_count = separate_list_count.filter(civil_status__icontains = civil_status)
    if assignment:
            separate_list_count = separate_list_count.filter(assignment = assignment)
    if office:
            separate_list_count = separate_list_count.filter(office = office)
    if service:
            separate_list_count = separate_list_count.filter(service = service)

    separate_list_count = separate_list_count.filter(emp_type="Separated").order_by('surname').count()


    separate_list = Personal.objects.all()
    if sex:
            separate_list = separate_list.filter(sex = sex)
    if civil_status:
            separate_list = separate_list.filter(civil_status__icontains = civil_status)
    if assignment:
            separate_list = separate_list.filter(assignment = assignment)
    if office:
            separate_list = separate_list.filter(office = office)
    if service:
            separate_list = separate_list.filter(service = service)

    separate_list = separate_list.filter(emp_type="Separated").order_by('surname')


    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/separate.html', {'Filter': Filter, 'separate_list': separate_list, 'separate_list_count': separate_list_count , 'sex': sex , 'civil_status': civil_status , 'assignment': assignment})
    else:
        return redirect('/pds')

@login_required
def FAFilter(request):
    Filter = "True"
    emp = request.POST['emp_type']
    civil_status = request.POST['civil_status']
    assignment = request.POST['assignment']
    office = request.POST['office']
    service = request.POST['service']


    approval = Personal.objects.all().order_by('id')
    
    if emp:
            approval = approval.filter(emp_type = emp)
    if civil_status:
            approval = approval.filter(civil_status__icontains = civil_status)
    if assignment:
            approval = approval.filter(assignment = assignment)
    if office:
            approval = approval.filter(office = office)
    if service:
            approval = approval.filter(service = service)

    approval = approval.filter(Q(status="For Approval") | Q(status="Disapproved")).order_by('surname').count()


    for_approval_list = Personal.objects.all()
    if emp:
            for_approval_list = for_approval_list.filter(emp_type = emp)
    if civil_status:
            for_approval_list = for_approval_list.filter(civil_status__icontains = civil_status)
    if assignment:
            for_approval_list = for_approval_list.filter(assignment = assignment)
    if office:
            for_approval_list = for_approval_list.filter(office = office)
    if service:
            for_approval_list = for_approval_list.filter(service = service)

    for_approval_list = for_approval_list.filter(Q(status="For Approval") | Q(status="Disapproved")).order_by('surname')


    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/hr/forapproval.html', {'Filter': Filter, 'for_approval_list': for_approval_list, 'approval': approval , 'emp': emp , 'civil_status': civil_status , 'assignment': assignment})
    else:
        return redirect('/pds')

@login_required
def CaapPayroll(request):
    payroll = Payroll.objects.all()

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required
def CreatePayroll(request):
    if request.user.groups.filter(name='payroll'):
            if request.method == "POST":
                pay701 = float(request.POST['pay_701'])
                basicSalary = float(request.POST['gross'])
                pay731 = round(pay701 * 0.12, 2)
                pay732 = 100.00
                if  float(request.POST['pay_733']):
                    if basicSalary > 80000.00:
                        pay733 = 1600.00
                    else:
                        pay733 = basicSalary * 0.04 / 2
                else:
                    pay733 = float(request.POST['pay_733'])              
                pay734 = 100.00
                pay413_1 = round(pay701 * 0.09, 2)
                if  float(request.POST['pay_414_1']):
                    pay414_1 = 100.00
                else:
                    pay414_1 = float(request.POST['pay_414_1'])
                pay415 = pay733
                pay711 = 2000.00 
                deductions =  float(request.POST['pay_415_a']) + float(request.POST['pay_412']) + float(request.POST['pay_415_a'])+ pay413_1 + pay414_1 + pay415  + float(request.POST['pay_439_6']) + float(request.POST['pay_413_2']) + float(request.POST['pay_413_3']) + float(request.POST['pay_413_5']) + float(request.POST['pay_413_6']) + float(request.POST['pay_413_11e']) + float(request.POST['pay_413_14']) + float(request.POST['pay_413_15']) + float(request.POST['pay_413_16']) + float(request.POST['pay_413_17']) + float(request.POST['pay_413_18']) + float(request.POST['pay_413_19']) + float(request.POST['pay_413_20']) + float(request.POST['pay_414_1a']) + float(request.POST['pay_414_2']) + float(request.POST['pay_414_2a']) + float(request.POST['pay_414_3']) + float(request.POST['pay_414_3a']) + float(request.POST['pay_439_8']) + float(request.POST['pay_439_9']) + float(request.POST['pay_439_10']) + float(request.POST['pay_439_10a']) + float(request.POST['pay_439_10b']) + float(request.POST['pay_439_12']) + float(request.POST['pay_439_13']) + float(request.POST['pay_439_16']) + float(request.POST['pay_439_18']) + float(request.POST['pay_439_19']) + float(request.POST['pay_439_21']) + float(request.POST['pay_439_22']) + float(request.POST['pay_439_28']) + float(request.POST['pay_439_33']) + float(request.POST['pay_439_34']) + float(request.POST['pay_439_35']) + float(request.POST['pay_146']) + float(request.POST['pay_148']) + float(request.POST['pay_149_tax'])
                netpay = pay701 - deductions
                pay111_07 = netpay + pay711
                pay15th = round(pay111_07/2 , 2)
                pay30th = pay111_07 - pay15th
                payTotal = pay15th + pay30th
                # return HttpResponse(pay731)
                form = PayrollForm(request.POST)
                if form.is_valid():
                        instance = form.save(commit=False)
                        instance.payroll_id = request.POST['payroll']
                        instance.personal_id = request.POST['pds'] 
                        instance.pay_731 = pay731
                        instance.pay_732 = pay732
                        instance.pay_733 = pay733
                        instance.pay_734 = pay734
                        instance.pay_413_1 = pay413_1
                        instance.pay_414_1 = pay414_1
                        instance.pay_415 = pay415
                        instance.deduc = deductions
                        instance.netpay = netpay
                        instance.pay_711 = pay711
                        instance.pay_111_07 = pay111_07
                        instance.pay_15th = pay15th
                        instance.pay_30th = pay30th
                        instance.total = payTotal
                        if request.POST['gross'] == 0.00:
                            instance.gross = pay701
                        else:
                            instance.gross =  request.POST['gross']
                        instance.save()
                        return redirect('/pds/payroll')
            form = PayrollForm(request.POST)
            return render(request,'pds/payroll/create.html',{'form':form})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required
def EditPayroll(request, id):
    if request.user.groups.filter(name='payroll'):
            payroll = Payroll.objects.get(id=id)
            form = PayrollForm(request.POST, instance=payroll)
            if request.user.groups.filter(name='payroll'):
                if request.POST:
                    payroll = Payroll.objects.get(id=id)
                    if form.is_valid():
                            if payroll.pay_701 == request.POST['pay_701']:
                                deductions =  float(request.POST['pay_415_a']) + float(request.POST['pay_412']) + float(request.POST['pay_413_1']) +float(request.POST['pay_415_a'])+ float(request.POST['pay_414_1']) + float(request.POST['pay_415']) + float(request.POST['pay_439_6']) + float(request.POST['pay_413_2']) + float(request.POST['pay_413_3']) + float(request.POST['pay_413_5']) + float(request.POST['pay_413_6']) + float(request.POST['pay_413_11e']) + float(request.POST['pay_413_14']) + float(request.POST['pay_413_15']) + float(request.POST['pay_413_16']) + float(request.POST['pay_413_17']) + float(request.POST['pay_413_18']) + float(request.POST['pay_413_19']) + float(request.POST['pay_413_20']) + float(request.POST['pay_414_1a']) + float(request.POST['pay_414_2']) + float(request.POST['pay_414_2a']) + float(request.POST['pay_414_3']) + float(request.POST['pay_414_3a']) + float(request.POST['pay_439_8']) + float(request.POST['pay_439_9']) + float(request.POST['pay_439_10']) + float(request.POST['pay_439_10a']) + float(request.POST['pay_439_10b']) + float(request.POST['pay_439_12']) + float(request.POST['pay_439_13']) + float(request.POST['pay_439_16']) + float(request.POST['pay_439_18']) + float(request.POST['pay_439_19']) + float(request.POST['pay_439_21']) + float(request.POST['pay_439_22']) + float(request.POST['pay_439_28']) + float(request.POST['pay_439_33']) + float(request.POST['pay_439_34']) + float(request.POST['pay_439_35']) + float(request.POST['pay_146']) + float(request.POST['pay_148']) + float(request.POST['pay_149_tax']) 
                                netpay = float(request.POST['pay_701']) + float(request.POST['rata']) - deductions
                                pay111_07 = netpay + float(request.POST['pay_711'])
                                pay15th = round(pay111_07/2 , 2)
                                pay30th = pay111_07 - pay15th
                                payTotal = pay15th + pay30th
                                payroll = Payroll.objects.get(id=id)
                                # save Update
                                instance = form.save(commit=False)
                                instance.id = id
                                instance.payroll_id = request.POST['payroll']
                                instance.personal_id = request.POST['personal'] 
                                instance.deduc = deductions
                                instance.netpay = netpay 
                                instance.pay_111_07 = pay111_07
                                instance.pay_15th = pay15th
                                instance.pay_30th = pay30th
                                instance.total = payTotal
                                instance.gross =  request.POST['gross']
                                instance.edited_by = request.user.username
                                instance.save() 
                                if request.POST['office'] == 'AANSOO':
                                    return redirect('/pds/aansoo_payroll')
                                elif request.POST['office'] == 'ANS':
                                    return redirect('/pds/ans_payroll')
                                elif request.POST['office'] == 'ADMS':
                                    return redirect('/pds/adms_payroll')
                                elif request.POST['office'] == 'ATS':
                                    return redirect('/pds/ats_payroll')
                                elif request.POST['office'] == 'CATC':
                                    return redirect('/pds/catc_payroll')
                                elif request.POST['office'] == 'CSIS':
                                    return redirect('/pds/csis_payroll')
                                elif request.POST['office'] == 'ELS':
                                    return redirect('/pds/els_payroll')
                                elif request.POST['office'] == 'FICG':
                                    return redirect('/pds/ficg_payroll')
                                elif request.POST['office'] == 'FD':
                                    return redirect('/pds/fmd_payroll')
                                elif request.POST['office'] == 'FSIS':
                                    return redirect('/pds/fsis_payroll')
                                elif request.POST['office'] == 'IAS':
                                    return redirect('/pds/ias_payroll')
                                elif request.POST['office'] == 'ODG':
                                    return redirect('/pds/odg_payroll')
                                elif request.POST['office'] == 'OFSAM':
                                    return redirect('/pds/ofsam_payroll')
                                elif request.POST['office'] == 'ADMIN':
                                    return redirect('/pds/admin_payroll')
                                else:
                                    return redirect('/pds/payroll')
                            else:
                                # Variable Declarations
                                pay701 = float(request.POST['pay_701'])
                                basicSalary = float(request.POST['gross'])
                                pay731 = round(pay701 * 0.12, 2)
                                pay732 = 100.00
                                if basicSalary > 80000.00:
                                    pay733 = 1600.00
                                else:
                                    pay733 = basicSalary * 0.04 / 2
                                pay734 = 100.00
                                pay413_1 = round(pay701 * 0.09, 2)
                                if float(request.POST['pay_414_1']) == "":
                                    pay414_1 = 100.00
                                else:
                                    pay414_1 = float(request.POST['pay_414_1'])
                                if float(request.POST['pay_415']) == "":                                   
                                    pay415 = pay733
                                else:
                                    pay415 = float(request.POST['pay_415'])
                                pay415 = pay733
                                pay711 = float(request.POST['pay_711']) 
                                deductions =  float(request.POST['pay_415_a']) + float(request.POST['pay_412']) + float(request.POST['pay_413_1']) +float(request.POST['pay_415_a'])+ float(request.POST['pay_414_1']) + float(request.POST['pay_415']) + float(request.POST['pay_439_6']) + float(request.POST['pay_413_2']) + float(request.POST['pay_413_3']) + float(request.POST['pay_413_5']) + float(request.POST['pay_413_6']) + float(request.POST['pay_413_11e']) + float(request.POST['pay_413_14']) + float(request.POST['pay_413_15']) + float(request.POST['pay_413_16']) + float(request.POST['pay_413_17']) + float(request.POST['pay_413_18']) + float(request.POST['pay_413_19']) + float(request.POST['pay_413_20']) + float(request.POST['pay_414_1a']) + float(request.POST['pay_414_2']) + float(request.POST['pay_414_2a']) + float(request.POST['pay_414_3']) + float(request.POST['pay_414_3a']) + float(request.POST['pay_439_8']) + float(request.POST['pay_439_9']) + float(request.POST['pay_439_10']) + float(request.POST['pay_439_10a']) + float(request.POST['pay_439_10b']) + float(request.POST['pay_439_12']) + float(request.POST['pay_439_13']) + float(request.POST['pay_439_16']) + float(request.POST['pay_439_18']) + float(request.POST['pay_439_19']) + float(request.POST['pay_439_21']) + float(request.POST['pay_439_22']) + float(request.POST['pay_439_28']) + float(request.POST['pay_439_33']) + float(request.POST['pay_439_34']) + float(request.POST['pay_439_35']) + float(request.POST['pay_146']) + float(request.POST['pay_148']) + float(request.POST['pay_149_tax'])
                                netpay = pay701  + float(request.POST['rata']) - deductions
                                pay111_07 = netpay + pay711
                                pay15th = round(pay111_07/2 , 2)
                                pay30th = pay111_07 - pay15th
                                payTotal = pay15th + pay30th
                                instance = form.save(commit=False)
                                instance.id = id
                                instance.payroll_id = request.POST['payroll']
                                instance.personal_id = request.POST['personal'] 
                                # instance.pay_731 = pay731
                                # instance.pay_732 = pay732
                                # instance.pay_733 = pay733
                                # instance.pay_734 = pay734
                                # instance.pay_413_1 = pay413_1
                                # instance.pay_414_1 = float(request.POST['pay_414_1'])
                                # instance.pay_415  = float(request.POST['pay_415'])
                                instance.deduc = deductions
                                instance.netpay = netpay
                                # instance.pay_711 = pay711
                                instance.pay_111_07 = pay111_07
                                instance.pay_15th = pay15th
                                instance.pay_30th = pay30th
                                instance.total = payTotal
                                instance.gross = request.POST['gross']
                                instance.save()
                                if request.POST['office'] == 'AANSOO':
                                    return redirect('/pds/aansoo_payroll')
                                elif request.POST['office'] == 'ANS':
                                    return redirect('/pds/ans_payroll')
                                elif request.POST['office'] == 'ADMS':
                                    return redirect('/pds/adms_payroll')
                                elif request.POST['office'] == 'ATS':
                                    return redirect('/pds/ats_payroll')
                                elif request.POST['office'] == 'CATC':
                                    return redirect('/pds/catc_payroll')
                                elif request.POST['office'] == 'CSIS':
                                    return redirect('/pds/csis_payroll')
                                elif request.POST['office'] == 'ELS':
                                    return redirect('/pds/els_payroll')
                                elif request.POST['office'] == 'FICG':
                                    return redirect('/pds/ficg_payroll')
                                elif request.POST['office'] == 'FD':
                                    return redirect('/pds/fmd_payroll')
                                elif request.POST['office'] == 'FSIS':
                                    return redirect('/pds/fsis_payroll')
                                elif request.POST['office'] == 'IAS':
                                    return redirect('/pds/ias_payroll')
                                elif request.POST['office'] == 'ODG':
                                    return redirect('/pds/odg_payroll')
                                elif request.POST['office'] == 'OFSAM':
                                    return redirect('/pds/ofsam_payroll')
                                elif request.POST['office'] == 'ADMIN':
                                    return redirect('/pds/admin_payroll')
                                else:
                                    return redirect('/pds/payroll')
                    context = {'payroll':payroll,'form':form }
                    return render(request,'pds/payroll/edit.html', context)
                form1 = PayrollForm(request.POST)
                return render(request,'pds/payroll/edit.html', {'payroll':payroll, 'form1':form1})
            else:
                return HttpResponseRedirect(reverse('pds:index'))
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

@login_required
def CreatePayroll2(request):
    if request.user.groups.filter(name='payroll'):
            if request.method == "POST":
                pay701 = float(request.POST['pay_701'])
                basicSalary = float(request.POST['gross'])
                pay731 = round(pay701 * 0.12, 2)
                pay732 = 100.00
                if  float(request.POST['pay_733']):
                    if basicSalary > 80000.00:
                        pay733 = 1600.00
                    else:
                        pay733 = basicSalary * 0.04 / 2
                else:
                    pay733 = float(request.POST['pay_733'])              
                pay734 = 100.00
                pay413_1 = round(pay701 * 0.09, 2)
                if  float(request.POST['pay_414_1']):
                    pay414_1 = 100.00
                else:
                    pay414_1 = float(request.POST['pay_414_1'])
                pay415 = pay733
                pay711 = 2000.00 
                deductions =  float(request.POST['pay_733_a']) + float(request.POST['pay_801']) + float(request.POST['pay_412']) + float(request.POST['pay_415_a'])+ pay413_1 + pay414_1 + pay415  + float(request.POST['pay_439_6']) + float(request.POST['pay_413_2']) + float(request.POST['pay_413_3']) + float(request.POST['pay_413_5']) + float(request.POST['pay_413_6']) + float(request.POST['pay_413_11e']) + float(request.POST['pay_413_14']) + float(request.POST['pay_413_15']) + float(request.POST['pay_413_16']) + float(request.POST['pay_413_17']) + float(request.POST['pay_413_18']) + float(request.POST['pay_413_19']) + float(request.POST['pay_413_20']) + float(request.POST['pay_414_1a']) + float(request.POST['pay_414_2']) + float(request.POST['pay_414_2a']) + float(request.POST['pay_414_3']) + float(request.POST['pay_414_3a']) + float(request.POST['pay_439_8']) + float(request.POST['pay_439_9']) + float(request.POST['pay_439_10']) + float(request.POST['pay_439_10a']) + float(request.POST['pay_439_10b']) + float(request.POST['pay_439_12']) + float(request.POST['pay_439_13']) + float(request.POST['pay_439_16']) + float(request.POST['pay_439_18']) + float(request.POST['pay_439_19']) + float(request.POST['pay_439_21']) + float(request.POST['pay_439_22']) + float(request.POST['pay_439_28']) + float(request.POST['pay_439_33']) + float(request.POST['pay_439_34']) + float(request.POST['pay_439_35']) + float(request.POST['pay_146']) + float(request.POST['pay_148']) + float(request.POST['pay_149_tax'])
                netpay = pay701 - deductions
                pay111_07 = netpay + pay711
                pay15th = round(pay111_07/2 , 2)
                pay30th = pay111_07 - pay15th
                payTotal = pay15th + pay30th
                # return HttpResponse(pay731)
                form = PayrollForm(request.POST)
                if form.is_valid():
                        instance = form.save(commit=False)
                        # instance.payroll_id = request.POST['payroll']
                        # instance.personal_id = request.POST['pds'] 
                        instance.pay_731 = pay731
                        instance.pay_732 = pay732
                        instance.pay_733 = pay733
                        instance.pay_734 = pay734
                        instance.pay_413_1 = pay413_1
                        instance.pay_414_1 = pay414_1
                        instance.pay_415 = pay415
                        instance.deduc = deductions
                        instance.netpay = netpay
                        instance.pay_711 = pay711
                        instance.pay_111_07 = pay111_07
                        instance.pay_15th = pay15th
                        instance.pay_30th = pay30th
                        instance.total = payTotal
                        if request.POST['gross'] == 0.00:
                            instance.gross = pay701
                        else:
                            instance.gross =  request.POST['gross']
                        instance.save()
                        return redirect('/pds/payroll')
            form = PayrollForm(request.POST)
            return render(request,'pds/payroll/create2.html',{'form':form})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required
def EditPayroll2(request, id):
    if request.user.groups.filter(name='payroll'):
            payroll = Payroll.objects.get(id=id)
            form = PayrollForm(request.POST, instance=payroll)
            if request.user.groups.filter(name='payroll'):
                if request.POST:
                    payroll = Payroll.objects.get(id=id)
                    if form.is_valid():
                            if payroll.pay_701 == request.POST['pay_701']:
                                deductions =  float(request.POST['pay_733_a']) + float(request.POST['pay_801']) + float(request.POST['pay_412']) + float(request.POST['pay_413_1']) +float(request.POST['pay_415_a'])+ float(request.POST['pay_414_1']) + float(request.POST['pay_415']) + float(request.POST['pay_439_6']) + float(request.POST['pay_413_2']) + float(request.POST['pay_413_3']) + float(request.POST['pay_413_5']) + float(request.POST['pay_413_6']) + float(request.POST['pay_413_11e']) + float(request.POST['pay_413_14']) + float(request.POST['pay_413_15']) + float(request.POST['pay_413_16']) + float(request.POST['pay_413_17']) + float(request.POST['pay_413_18']) + float(request.POST['pay_413_19']) + float(request.POST['pay_413_20']) + float(request.POST['pay_414_1a']) + float(request.POST['pay_414_2']) + float(request.POST['pay_414_2a']) + float(request.POST['pay_414_3']) + float(request.POST['pay_414_3a']) + float(request.POST['pay_439_8']) + float(request.POST['pay_439_9']) + float(request.POST['pay_439_10']) + float(request.POST['pay_439_10a']) + float(request.POST['pay_439_10b']) + float(request.POST['pay_439_12']) + float(request.POST['pay_439_13']) + float(request.POST['pay_439_16']) + float(request.POST['pay_439_18']) + float(request.POST['pay_439_19']) + float(request.POST['pay_439_21']) + float(request.POST['pay_439_22']) + float(request.POST['pay_439_28']) + float(request.POST['pay_439_33']) + float(request.POST['pay_439_34']) + float(request.POST['pay_439_35']) + float(request.POST['pay_146']) + float(request.POST['pay_148']) + float(request.POST['pay_149_tax']) 
                                netpay = float(request.POST['pay_701']) - deductions
                                pay111_07 = netpay + float(request.POST['pay_711'])
                                pay15th = round(pay111_07/2 , 2)
                                pay30th = pay111_07 - pay15th
                                payTotal = pay15th + pay30th
                                payroll = Payroll.objects.get(id=id)
                                # save Update
                                instance = form.save(commit=False)
                                instance.id = id
                                # instance.payroll_id = payroll.payroll_id
                                # instance.personal_id = payroll.personal_id
                                instance.deduc = deductions
                                instance.netpay = netpay 
                                instance.pay_111_07 = pay111_07
                                instance.pay_15th = pay15th
                                instance.pay_30th = pay30th
                                instance.total = payTotal
                                instance.gross =  request.POST['gross']
                                instance.edited_by = request.user.username
                                instance.save()
                                if request.POST['office'] == 'AANSOO':
                                    return redirect('/pds/aansoo_payroll')
                                elif request.POST['office'] == 'ANS':
                                    return redirect('/pds/ans_payroll')
                                elif request.POST['office'] == 'ADMS':
                                    return redirect('/pds/adms_payroll')
                                elif request.POST['office'] == 'ATS':
                                    return redirect('/pds/ats_payroll')
                                elif request.POST['office'] == 'CATC':
                                    return redirect('/pds/catc_payroll')
                                elif request.POST['office'] == 'CSIS':
                                    return redirect('/pds/csis_payroll')
                                elif request.POST['office'] == 'ELS':
                                    return redirect('/pds/els_payroll')
                                elif request.POST['office'] == 'FICG':
                                    return redirect('/pds/ficg_payroll')
                                elif request.POST['office'] == 'FMD':
                                    return redirect('/pds/fmd_payroll')
                                elif request.POST['office'] == 'FSIS':
                                    return redirect('/pds/fsis_payroll')
                                elif request.POST['office'] == 'IAS':
                                    return redirect('/pds/ias_payroll')
                                elif request.POST['office'] == 'ODG':
                                    return redirect('/pds/odg_payroll')
                                elif request.POST['office'] == 'OFSAM':
                                    return redirect('/pds/ofsam_payroll')
                                elif request.POST['office'] == 'ADMIN':
                                    return redirect('/pds/admin_payroll')
                                else:
                                    return redirect('/pds/payroll')
                            else:
                                # Variable Declarations
                                pay701 = float(request.POST['pay_701'])
                                basicSalary = float(request.POST['gross'])
                                pay731 = round(pay701 * 0.12, 2)
                                pay732 = 100.00
                                if basicSalary > 80000.00:
                                    pay733 = 1600.00
                                else:
                                    pay733 = basicSalary * 0.04 / 2
                                pay734 = 100.00
                                pay413_1 = round(pay701 * 0.09, 2)
                                if float(request.POST['pay_414_1']) == "":
                                    pay414_1 = 100.00
                                else:
                                    pay414_1 = float(request.POST['pay_414_1'])
                                if float(request.POST['pay_415']) == "":                                   
                                    pay415 = pay733
                                else:
                                    pay415 = float(request.POST['pay_415'])
                                pay415 = pay733
                                pay711 = float(request.POST['pay_711']) 
                                deductions =  float(request.POST['pay_733_a']) + float(request.POST['pay_801']) + float(request.POST['pay_412']) + float(request.POST['pay_413_1']) +float(request.POST['pay_415_a'])+ float(request.POST['pay_414_1']) + float(request.POST['pay_415']) + float(request.POST['pay_439_6']) + float(request.POST['pay_413_2']) + float(request.POST['pay_413_3']) + float(request.POST['pay_413_5']) + float(request.POST['pay_413_6']) + float(request.POST['pay_413_11e']) + float(request.POST['pay_413_14']) + float(request.POST['pay_413_15']) + float(request.POST['pay_413_16']) + float(request.POST['pay_413_17']) + float(request.POST['pay_413_18']) + float(request.POST['pay_413_19']) + float(request.POST['pay_413_20']) + float(request.POST['pay_414_1a']) + float(request.POST['pay_414_2']) + float(request.POST['pay_414_2a']) + float(request.POST['pay_414_3']) + float(request.POST['pay_414_3a']) + float(request.POST['pay_439_8']) + float(request.POST['pay_439_9']) + float(request.POST['pay_439_10']) + float(request.POST['pay_439_10a']) + float(request.POST['pay_439_10b']) + float(request.POST['pay_439_12']) + float(request.POST['pay_439_13']) + float(request.POST['pay_439_16']) + float(request.POST['pay_439_18']) + float(request.POST['pay_439_19']) + float(request.POST['pay_439_21']) + float(request.POST['pay_439_22']) + float(request.POST['pay_439_28']) + float(request.POST['pay_439_33']) + float(request.POST['pay_439_34']) + float(request.POST['pay_439_35']) + float(request.POST['pay_146']) + float(request.POST['pay_148']) + float(request.POST['pay_149_tax'])
                                netpay = pay701 - deductions
                                pay111_07 = netpay + pay711
                                pay15th = round(pay111_07/2 , 2)
                                pay30th = pay111_07 - pay15th
                                payTotal = pay15th + pay30th
                                instance = form.save(commit=False)
                                instance.id = id
                                # instance.payroll_id = payroll.payroll_id
                                # instance.personal_id = payroll.personal_id
                                # instance.pay_731 = pay731
                                # instance.pay_732 = pay732
                                # instance.pay_733 = pay733
                                # instance.pay_734 = pay734
                                # instance.pay_413_1 = pay413_1
                                # instance.pay_414_1 = float(request.POST['pay_414_1'])
                                # instance.pay_415  = float(request.POST['pay_415'])
                                instance.deduc = deductions
                                instance.netpay = netpay
                                # instance.pay_711 = pay711
                                instance.pay_111_07 = pay111_07
                                instance.pay_15th = pay15th
                                instance.pay_30th = pay30th
                                instance.total = payTotal
                                instance.gross = request.POST['gross']
                                instance.save()
                                if request.POST['office'] == 'AANSOO':
                                    return redirect('/pds/aansoo_payroll')
                                elif request.POST['office'] == 'ANS':
                                    return redirect('/pds/ans_payroll')
                                elif request.POST['office'] == 'ADMS':
                                    return redirect('/pds/adms_payroll')
                                elif request.POST['office'] == 'ATS':
                                    return redirect('/pds/ats_payroll')
                                elif request.POST['office'] == 'CATC':
                                    return redirect('/pds/catc_payroll')
                                elif request.POST['office'] == 'CSIS':
                                    return redirect('/pds/csis_payroll')
                                elif request.POST['office'] == 'ELS':
                                    return redirect('/pds/els_payroll')
                                elif request.POST['office'] == 'FICG':
                                    return redirect('/pds/ficg_payroll')
                                elif request.POST['office'] == 'FMD':
                                    return redirect('/pds/fmd_payroll')
                                elif request.POST['office'] == 'FSIS':
                                    return redirect('/pds/fsis_payroll')
                                elif request.POST['office'] == 'IAS':
                                    return redirect('/pds/ias_payroll')
                                elif request.POST['office'] == 'ODG':
                                    return redirect('/pds/odg_payroll')
                                elif request.POST['office'] == 'OFSAM':
                                    return redirect('/pds/ofsam_payroll')
                                elif request.POST['office'] == 'ADMIN':
                                    return redirect('/pds/admin_payroll')
                                else:
                                    return redirect('/pds/payroll')
                    context = {'payroll':payroll,'form':form }
                    return render(request,'pds/payroll/edit2.html', context)
                form1 = PayrollForm(request.POST)
                return render(request,'pds/payroll/edit2.html', {'payroll':payroll, 'form1':form1})
            else:
                return HttpResponseRedirect(reverse('pds:index'))
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')
# def Updatepayroll(request, id):
    
#         return render(request,'pds/payroll/edit.html', {'form':form, 'payroll': payroll})
#     return redirect('/pds/payroll')

# View Users

@login_required
def UsersView(request):
    users = User.objects.all()
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/users/index.html', {'users':users})
    else:
        return redirect('/pds')
    

# Edit Users
@login_required
def UsersEdit(request, id):
    data = User.objects.get(id=id)

    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/users/edit.html', {'data': data})
    else:
        return redirect('/pds')

@login_required
def UsersUpdate(request, id):
    data = User.objects.get(id=id)
    form = UserForm(request.POST, instance=data)
    if request.user.groups.filter(name='hrmd'):
        if request.POST:       
            instance = User.objects.get(id=id)
            instance.id = id
            instance.is_active = request.POST['is_active']
            instance.save()
            return redirect('/pds/users_list')
        return render(request,'pds/users/edit.html', {'data':data})
    else:
        return redirect('/pds')
    


# PDS Sheet Pages
@login_required
def Page1(request, id):
    pds = Personal.objects.filter(id=id).first()
    children = Children.objects.filter(child_id=pds.id).order_by('-birth_date')
    childs = Children.objects.filter(child_id=pds.id).count()
    education = Education.objects.filter(education_id=pds.id).order_by('date_from')
    educs = Education.objects.filter(education_id=pds.id).count()
    today = datetime.date.today()
    context = {'pds': pds, 'children': children, 'childs' : childs,'educs' : educs, 'education': education ,'today': today}
    
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/pages/page1.html', context)
    else:
        return redirect('/pds')

@login_required
def Page2(request, id):
    pds = Personal.objects.filter(id=id).first()
    eligible = Eligibility.objects.filter(eligible_id=pds.id)
    elig = Eligibility.objects.filter(eligible_id=pds.id).count()
    experience = Experience.objects.filter(exp_id=pds.id).order_by('-exp_to')
    exp = Experience.objects.filter(exp_id=pds.id).count()
    today = datetime.date.today()
    context = {'pds': pds,'eligible': eligible, 'elig': elig, 'experience': experience, 'exp': exp,'today': today}
    
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/pages/page2.html', context)
    else:
        return redirect('/pds')

@login_required
def Page3(request, id):
    pds = Personal.objects.filter(id=id).first()
    voluntary = Voluntary.objects.filter(voluntary_id=pds.id)
    volun = Voluntary.objects.filter(voluntary_id=pds.id).count()
    learning = Learning.objects.filter(learn_id=pds.id).exclude(is_approve='For Review')
    learn = Learning.objects.filter(learn_id=pds.id).exclude(is_approve='For Review').count()

    other_skills = Other_skills.objects.filter(ski_id=pds.id)
    skills = Other_skills.objects.filter(ski_id=pds.id).count()
    other_recognitions = Other_recognitions.objects.filter(recog_id=pds.id)
    recognitions = Other_recognitions.objects.filter(recog_id=pds.id).count()
    other_membership = Other_membership.objects.filter(member_id=pds.id)
    membership = Other_membership.objects.filter(member_id=pds.id).count()
    today = datetime.date.today()
    context = {'pds': pds,'voluntary': voluntary, 'volun': volun, 'learning': learning, 'learn': learn, 'other_skills': other_skills, 'skills': skills, 'other_recognitions': other_recognitions, 'recognitions': recognitions, 'other_membership': other_membership, 'membership': membership,'today': today}
    
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/pages/page3.html', context)
    else:
        return redirect('/pds')

@login_required
def Page4(request, id):
    pds = Personal.objects.filter(id=id).first()
    otherinfo = Otherinfo.objects.filter(otherinfo_id=pds.id).first()
    refers = Refferences.objects.filter(refer_id=pds.id)[:3]
    refer_count = Refferences.objects.filter(refer_id=pds.id).count()
    today = datetime.date.today()

    context = {'pds': pds,'otherinfo': otherinfo,'refers': refers,'refer_count': refer_count,'today': today}
    
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/pages/page4.html', context)
    else:
        return redirect('/pds')
