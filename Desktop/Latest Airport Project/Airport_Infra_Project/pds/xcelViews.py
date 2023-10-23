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
import xlwt

# Create your views here.
from .models import Personal, Payroll, Children, Education, Eligibility, Experience, Voluntary, Learning, Otherinfo, Refferences, Other_skills, Other_recognitions, Other_membership, Vaccine, Training


# Export Users List
@login_required 
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First name', 'Last name', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
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
def export_permanents_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="permanents.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Permanent')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id','Status','Surname', 'First name', 'Middle name','Extension Name' , 'Birth Day','Birth Place','Sex', 'Office', 'Service','Civil Status','Height','Weight','Blood Type','GSIS','PAGIBG','Philhealth','TIN','Employee Number','Citizenship','Citizenship Detail','Citizenship Contry','Email','Salary Grade','Step Increment','Salary Rate','Item Number']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Personal.objects.all().values_list('id','emp_type','surname', 'first_name', 'middle_name', 'ext_name','birth_date','birth_place','sex' , 'office','service','civil_status','height','weight','blood_type','gsis','pagibig','philhealth','tin','emp_number','citizenship','citizen_detail','citizen_country','email','salary_grade','step','rate','item')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    if request.user.groups.filter(name='hrmd'):
        return response
    else:
        return HttpResponseRedirect(reverse('pds:index'))

# payroll
@login_required 
def export_payroll_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="payroll.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Payroll')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.all().values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    if request.user.groups.filter(name='hrmd'):
        return response
    else:
        return HttpResponseRedirect(reverse('pds:index'))

# Payroll Per Office
@login_required 
def export_payroll2_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Payroll.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
# AANSOO
    ws = wb.add_sheet('AANSOO')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='AANSOO').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
# ADMIN
    ws = wb.add_sheet('ADMIN')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='ADMIN').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
# ADMS
    ws = wb.add_sheet('ADMS')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='ADMS').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# ANS
    ws = wb.add_sheet('ANS')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='ANS').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# ATS
    ws = wb.add_sheet('ATS')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='ATS').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# CATC
    ws = wb.add_sheet('CATC')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='CATC').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# CSIS
    ws = wb.add_sheet('CSIS')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='CSIS').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# FICG
    ws = wb.add_sheet('FICG')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='FICG').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# FSIS
    ws = wb.add_sheet('FSIS')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='FSIS').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# FMD
    ws = wb.add_sheet('FMD')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='FMD').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# IAS
    ws = wb.add_sheet('IAS')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='IAS').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# ODG
    ws = wb.add_sheet('ODG')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='ODG').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# OFSAM
    ws = wb.add_sheet('OFSAM')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='OFSAM').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

# ELS
    ws = wb.add_sheet('ELS')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Payroll.objects.filter(office='ELS').values_list('surname','first_name','office','pay_731','pay_732','pay_733','pay_734','pay_701','pay_412','pay_413_1','pay_414_1','pay_415','pay_439_6','pay_413_2','pay_413_3','pay_413_5','pay_413_6','pay_413_11e','pay_413_14','pay_413_15','pay_413_16','pay_413_17','pay_413_18','pay_413_19','pay_413_20','pay_414_1a','pay_414_2','pay_414_2a','pay_414_3','pay_414_3a','pay_439_8','pay_439_9','pay_439_10','pay_439_10a','pay_439_10b','pay_439_12','pay_439_13','pay_439_16','pay_439_18','pay_439_19','pay_439_21','pay_439_22','pay_439_28','pay_439_33','pay_439_34','pay_439_35','pay_146','pay_148','pay_149_tax','pay_711','pay_749_osp','deduc','netpay','pay_111_07','pay_15th','pay_30th','total','remarks')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    if request.user.groups.filter(name='hrmd'):
        return response
    else:
        return HttpResponseRedirect(reverse('pds:index'))



