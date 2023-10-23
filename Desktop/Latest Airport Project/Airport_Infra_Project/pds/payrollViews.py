from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.template import loader
from django.urls import reverse
from django.template.loader import render_to_string, get_template 
from django.utils import timezone
from django.contrib import messages
from django.views import View
import datetime
from io import BytesIO
# PDF Import HTML to PDF
from xhtml2pdf import pisa 
from django.db.models import Sum

# Create your views here.
from .models import Personal, Payroll, Children, Education, Eligibility, Experience, Voluntary, Learning, Otherinfo, Refferences, Other_skills, Other_recognitions, Other_membership, Vaccine, Training, Signatory

@login_required
def PayrollPerOffice(request):
    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/payroll/list.html')
    else:
        return HttpResponseRedirect(reverse('pds:index'))
    
    

# PDFViews
# @login_required
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

today = datetime.datetime.now() 
month = today.strftime('%B')

payroll = Payroll.objects.all()
gov_share = Payroll.objects.values('pay_731').aggregate(Sum('pay_731')).get('pay_731__sum', 0.00)
mont_sal = Payroll.objects.values('pay_701').aggregate(Sum('pay_701')).get('pay_701__sum', 0.00)
emp_compen = Payroll.objects.values('pay_732').aggregate(Sum('pay_732')).get('pay_732__sum', 0.00)
pagibig_prem = Payroll.objects.values('pay_733').aggregate(Sum('pay_733')).get('pay_733__sum', 0.00)
philhealt_prem = Payroll.objects.values('pay_734').aggregate(Sum('pay_734')).get('pay_734__sum', 0.00)
p711 = Payroll.objects.values('pay_711').aggregate(Sum('pay_711')).get('pay_711__sum', 0.00)
p749 = Payroll.objects.values('pay_749_osp').aggregate(Sum('pay_749_osp')).get('pay_749_osp__sum', 0.00)
neto = Payroll.objects.values('netpay').aggregate(Sum('netpay')).get('netpay__sum', 0.00)
deduc = Payroll.objects.values('deduc').aggregate(Sum('deduc')).get('deduc__sum', 0.00)
total_due = Payroll.objects.values('pay_111_07').aggregate(Sum('pay_111_07')).get('pay_111_07__sum', 0.00)
p15th = Payroll.objects.values('pay_15th').aggregate(Sum('pay_15th')).get('pay_15th__sum', 0.00)
p30th = Payroll.objects.values('pay_30th').aggregate(Sum('pay_30th')).get('pay_30th__sum', 0.00)

# First Column Deductions
pay_412 = Payroll.objects.values('pay_412').aggregate(Sum('pay_412')).get('pay_412__sum', 0.00)
pay_413_1 = Payroll.objects.values('pay_413_1').aggregate(Sum('pay_413_1')).get('pay_413_1__sum', 0.00)
pay_414_1 = Payroll.objects.values('pay_414_1').aggregate(Sum('pay_414_1')).get('pay_414_1__sum', 0.00)
pay_415 = Payroll.objects.values('pay_415').aggregate(Sum('pay_415')).get('pay_415__sum', 0.00)
pay_439_6 = Payroll.objects.values('pay_439_6').aggregate(Sum('pay_439_6')).get('pay_439_6__sum', 0.00)
pay_413_2 = Payroll.objects.values('pay_413_2').aggregate(Sum('pay_413_2')).get('pay_413_2__sum', 0.00)
pay_413_3 = Payroll.objects.values('pay_413_3').aggregate(Sum('pay_413_3')).get('pay_413_3__sum', 0.00)
pay_413_5 = Payroll.objects.values('pay_413_5').aggregate(Sum('pay_413_5')).get('pay_413_5__sum', 0.00)
pay_413_6 = Payroll.objects.values('pay_413_6').aggregate(Sum('pay_413_6')).get('pay_413_6__sum', 0.00)
pay_413_11e = Payroll.objects.values('pay_413_11e').aggregate(Sum('pay_413_11e')).get('pay_413_11e__sum', 0.00)
pay_413_14 = Payroll.objects.values('pay_413_14').aggregate(Sum('pay_413_14')).get('pay_413_14__sum', 0.00)
# Row 1 Sum
deduc_row1 = pay_412 + pay_413_1 + pay_414_1 + pay_415 + pay_439_6 + pay_413_2 + pay_413_3 + pay_413_5 + pay_413_6 + pay_413_11e + pay_413_14 




# Second Column Deductions
pay_413_15 = Payroll.objects.values('pay_413_15').aggregate(Sum('pay_413_15')).get('pay_413_15__sum', 0.00)
pay_413_16 = Payroll.objects.values('pay_413_16').aggregate(Sum('pay_413_16')).get('pay_413_16__sum', 0.00)
pay_413_17 = Payroll.objects.values('pay_413_17').aggregate(Sum('pay_413_17')).get('pay_413_17__sum', 0.00)
pay_413_18 = Payroll.objects.values('pay_413_18').aggregate(Sum('pay_413_18')).get('pay_413_18__sum', 0.00)
pay_413_19 = Payroll.objects.values('pay_413_19').aggregate(Sum('pay_413_19')).get('pay_413_19__sum', 0.00)
pay_413_20 = Payroll.objects.values('pay_413_20').aggregate(Sum('pay_413_20')).get('pay_413_20__sum', 0.00)
pay_414_1a = Payroll.objects.values('pay_414_1a').aggregate(Sum('pay_414_1a')).get('pay_414_1a__sum', 0.00)
pay_414_2 = Payroll.objects.values('pay_414_2').aggregate(Sum('pay_414_2')).get('pay_414_2__sum', 0.00)
pay_414_2a = Payroll.objects.values('pay_414_2a').aggregate(Sum('pay_414_2a')).get('pay_414_2a__sum', 0.00)
pay_414_3 = Payroll.objects.values('pay_414_3').aggregate(Sum('pay_414_3')).get('pay_414_3__sum', 0.00)

# Row 2 Sum
deduc_row2 = pay_413_15 + pay_413_16 + pay_413_17 + pay_413_18 + pay_413_19 + pay_413_20 + pay_414_1a + pay_414_2 + pay_414_2a + pay_414_3



# Third Column Deductions
pay_414_3a = Payroll.objects.values('pay_414_3a').aggregate(Sum('pay_414_3a')).get('pay_414_3a__sum', 0.00)
pay_439_8 = Payroll.objects.values('pay_439_8').aggregate(Sum('pay_439_8')).get('pay_439_8__sum', 0.00)
pay_439_9 = Payroll.objects.values('pay_439_9').aggregate(Sum('pay_439_9')).get('pay_439_9__sum', 0.00)
pay_439_10 = Payroll.objects.values('pay_439_10').aggregate(Sum('pay_439_10')).get('pay_439_10__sum', 0.00)
pay_439_10a = Payroll.objects.values('pay_439_10a').aggregate(Sum('pay_439_10a')).get('pay_439_10a__sum', 0.00)
pay_439_10b = Payroll.objects.values('pay_439_10b').aggregate(Sum('pay_439_10b')).get('pay_439_10b__sum', 0.00)
pay_439_12 = Payroll.objects.values('pay_439_12').aggregate(Sum('pay_439_12')).get('pay_439_12__sum', 0.00)
pay_439_13 = Payroll.objects.values('pay_439_13').aggregate(Sum('pay_439_13')).get('pay_439_13__sum', 0.00)
pay_439_16 = Payroll.objects.values('pay_439_16').aggregate(Sum('pay_439_16')).get('pay_439_16__sum', 0.00)
pay_439_18 = Payroll.objects.values('pay_439_18').aggregate(Sum('pay_439_18')).get('pay_439_18__sum', 0.00)

# Row 3 Sum
deduc_row3 = pay_414_3a + pay_439_8 + pay_439_9 + pay_439_10 + pay_439_10a + pay_439_10b + pay_439_12 + pay_439_13 + pay_439_16 + pay_439_18

# Fouth Column Deductions
pay_439_19 = Payroll.objects.values('pay_439_19').aggregate(Sum('pay_439_19')).get('pay_439_19__sum', 0.00)
pay_439_21 = Payroll.objects.values('pay_439_21').aggregate(Sum('pay_439_21')).get('pay_439_21__sum', 0.00)
pay_439_22 = Payroll.objects.values('pay_439_22').aggregate(Sum('pay_439_22')).get('pay_439_22__sum', 0.00)
pay_439_28 = Payroll.objects.values('pay_439_28').aggregate(Sum('pay_439_28')).get('pay_439_28__sum', 0.00)
pay_439_33 = Payroll.objects.values('pay_439_33').aggregate(Sum('pay_439_33')).get('pay_439_33__sum', 0.00)
pay_439_34 = Payroll.objects.values('pay_439_34').aggregate(Sum('pay_439_34')).get('pay_439_34__sum', 0.00)
pay_439_35 = Payroll.objects.values('pay_439_35').aggregate(Sum('pay_439_35')).get('pay_439_35__sum', 0.00)
pay_146 = Payroll.objects.values('pay_146').aggregate(Sum('pay_146')).get('pay_146__sum', 0.00)
pay_148 = Payroll.objects.values('pay_148').aggregate(Sum('pay_148')).get('pay_148__sum', 0.00)
pay_149_tax = Payroll.objects.values('pay_149_tax').aggregate(Sum('pay_149_tax')).get('pay_149_tax__sum', 0.00)

# Row 4 Sum
deduc_row4 = pay_439_19 + pay_439_21 + pay_439_22 + pay_439_28 + pay_439_33 + pay_439_34 + pay_439_35 + pay_146 + pay_148 + pay_149_tax


sign = Signatory.objects.get(id= 1)

data = {
    "sign": sign,
    "payroll": payroll,
    "mont_sal": mont_sal,
    "gov_share": gov_share,
    "emp_compen": emp_compen,
    "pagibig_prem": pagibig_prem,
    "philhealt_prem": philhealt_prem,
    "p711": p711,
    "p749": p749,
    "neto": neto,
    "deduc": deduc,
    "deduc_row1": deduc_row1,
    "deduc_row2": deduc_row2,
    "deduc_row3": deduc_row3,
    "deduc_row4": deduc_row4,
    "total_due": total_due,
    "p15th": p15th,
    "p30th": p30th,
    "month": month,
    }



#Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):

        pdf = render_to_pdf('app/pdf_template.html', data)
        if request.user.groups.filter(name='hrmd'):
            return HttpResponse(pdf, content_type='application/pdf')
        else:
            return HttpResponseRedirect(reverse('pds:index'))


#Automaticly downloads to PDF file
# class DownloadPDF(View):
#     def get(self, request, *args, **kwargs):
        
#         pdf = render_to_pdf('app/pdf_template.html', data)

#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "Invoice_%s.pdf" %("12341231")
#         content = "attachment; filename='%s'" %(filename)
#         response['Content-Disposition'] = content
#         return response

@login_required 
def AANSOOPayroll(request):
    payroll = Payroll.objects.filter(office='AANSOO').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ADMSPayroll(request):
    payroll = Payroll.objects.filter(office='ADMS').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ANSPayroll(request):
    payroll = Payroll.objects.filter(office='ANS').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ATSPayroll(request):
    payroll = Payroll.objects.filter(office='ATS').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def CATCPayroll(request):
    payroll = Payroll.objects.filter(office='CATC').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def CSISPayroll(request):
    payroll = Payroll.objects.filter(office='CSIS').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ELSPayroll(request):
    payroll = Payroll.objects.filter(office='ELS').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def FICGPayroll(request):
    payroll = Payroll.objects.filter(office='FICG').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def FMDPayroll(request):
    payroll = Payroll.objects.filter(office='FD').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def FSISPayroll(request):
    payroll = Payroll.objects.filter(office='FSIS').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def IASPayroll(request):
    payroll = Payroll.objects.filter(office='IAS').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ODGPayroll(request):
    payroll = Payroll.objects.filter(office='ODG').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def OFSAMPayroll(request):
    payroll = Payroll.objects.filter(office='OFSAM').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ADMINPayroll(request):
    payroll = Payroll.objects.filter(office='ADMIN').order_by('surname')

    if request.user.groups.filter(name='payroll'):
        return render(request, 'pds/payroll/index.html', {'payroll':payroll})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')


