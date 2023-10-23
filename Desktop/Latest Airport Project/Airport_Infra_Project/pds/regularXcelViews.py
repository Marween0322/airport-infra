
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
from django.utils import timezone
import datetime
from datetime import date, timedelta
# importing the necessary libraries
from .process import html_to_pdf 
from django.views import generic 
from django.db.models import Q
import xlwt

# Create your views here.
from .models import Personal, Children, Education, Eligibility, Experience, Voluntary, Learning, Otherinfo, Refferences, Other_skills, Other_recognitions, Other_membership, Vaccine, Training


# Permanent
@login_required 
def export_permanents_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="permanents.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Permanent')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Surname', 'First name', 'Middle name','Extension Name' , 'Birth Day','Birth Place','Sex', 'Office', 'Service','Civil Status','Height','Weight','Blood Type','GSIS','PAGIBG','Philhealth','TIN','Employee Number','Citizenship','Citizenship Detail','Citizenship Contry','Email','Salary Grade','Step Increment','Salary Rate','Item Number']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Personal.objects.filter(Q(emp_type="Permanent")| Q(emp_type="Co-Terminus")| Q(emp_type="TEMPORARY") | Q(emp_type="PRESIDENTIAL APPOINTEE")).values_list('surname', 'first_name', 'middle_name', 'ext_name','birth_date','birth_place','sex' , 'office','service','civil_status','height','weight','blood_type','gsis','pagibig','philhealth','tin','emp_number','citizenship','citizen_detail','citizen_country','email','salary_grade','step','rate','item')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    if request.user.groups.filter(name='hrmd'):
        return response
    else:
        return HttpResponseRedirect(reverse('pds:index'))

# Permanent
@login_required 
def Export_Outsourced_Xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Outsourced.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Outsourced')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id','Status','Surname', 'First name', 'Middle name','Extension Name' , 'Birth Day','Birth Place','Sex', 'Office', 'Service','Civil Status','Height','Weight','Blood Type','GSIS','PAGIBG','Philhealth','TIN','Employee Number','Citizenship','Citizenship Detail','Citizenship Contry','Email','Salary Grade','Step Increment','Salary Rate','Item Number']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Personal.objects.filter(( Q(emp_type="Job Order") | Q(emp_type="Contract of Service") | Q(emp_type="Outsourced")) ).values_list('id','emp_type','surname', 'first_name', 'middle_name', 'ext_name','birth_date','birth_place','sex' , 'office','service','civil_status','height','weight','blood_type','gsis','pagibig','philhealth','tin','emp_number','citizenship','citizen_detail','citizen_country','email','salary_grade','step','rate','item')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    if request.user.groups.filter(name='hrmd'):
        return response
    else:
        return HttpResponseRedirect(reverse('pds:index'))



