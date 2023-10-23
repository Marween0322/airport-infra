from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils import timezone
import datetime
from django.db.models import Q
from datetime import date, timedelta
from django.contrib import messages
import xlwt

# Create your views here.
from .models import Personal, Payslipstatus, Payroll, January, February, March, April, May, June, July, August, September, October, November, December, Signatory, Bonuses
from .forms import BonusForm

@login_required
def ViewPayslip(request):
    jan = Payslipstatus.objects.get(month='January')
    feb = Payslipstatus.objects.get(month='February')
    march = Payslipstatus.objects.get(month='March')
    april = Payslipstatus.objects.get(month='April')
    may = Payslipstatus.objects.get(month='May')
    june = Payslipstatus.objects.get(month='June')
    july = Payslipstatus.objects.get(month='July')
    aug = Payslipstatus.objects.get(month='August')
    sept = Payslipstatus.objects.get(month='September')
    octb = Payslipstatus.objects.get(month='October')
    nov = Payslipstatus.objects.get(month='November')
    dec = Payslipstatus.objects.get(month='December')
    context = {'jan': jan, 'feb': feb, 'march': march, 'april': april, 'may': may, 'june': june, 'july': july, 'aug': aug, 'sept': sept, 'octb': octb, 'nov': nov, 'dec': dec,}
    return render(request, 'pds/payroll/view.html', context)


@login_required
def ViewJanuary(request):
    payroll = January.objects.filter(january_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "January"
        year = "2023"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewFebruary(request):
    payroll = February.objects.filter(february_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "February"
        year = "2023"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewMarch(request):
    payroll = March.objects.filter(march_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "March"
        year = "2023"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewApril(request):
    payroll = April.objects.filter(april_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "April"
        year = "2023"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewMay(request):
    payroll = May.objects.filter(may_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "May"
        year = "2023"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewJune(request):
    payroll = June.objects.filter(june_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "June"
        year = "2023"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewJuly(request):
    payroll = July.objects.filter(july_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "July"
        year = "2023"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewAugust(request):
    payroll = August.objects.filter(august_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "August"
        year = "2023"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewSeptember(request):
    payroll = September.objects.filter(september_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "September"
        year = "2023"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewOctober(request):
    payroll = October.objects.filter(october_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "October"
        year = "2022"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewNovember(request):
    payroll = November.objects.filter(november_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        bonus = Bonuses.objects.get(bonus_id=request.user.id)
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "November"
        year = "2022"
        if bonus.tax:
           bonusTax = bonus.tax
        else:     
            bonusTax = 0
        if bonus.patcomc:
           bonusPatcomc = bonus.patcomc
        else:     
            bonusPatcomc = 0
        if bonus.liquidation:
           bonusLiquidation = bonus.liquidation
        else:     
            bonusLiquidation = 0

        total_yeb = bonus.year_end_bonus - bonusTax - bonusPatcomc - bonusLiquidation
        total_year_end_bonus = total_yeb + bonus.cash_gift
        total_nov = payroll.pay_701 + payroll.pay_711 + total_year_end_bonus
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata + bonus.year_end_bonus + bonus.cash_gift

        return render(request, 'pds/payroll/november.html', {'total_nov':total_nov,'total_year_end_bonus':total_year_end_bonus,'bonus':bonus,'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')

@login_required
def ViewDecember(request):
    payroll = December.objects.filter(december_id=request.user.id).first()
    if payroll:
        pds = Personal.objects.filter(author=request.user).exclude(emp_type="Separated").exclude(Q(status="Disapproved") | Q(status="For Approval") ).first()
        today = datetime.datetime.now()
        today1 = datetime.date.today()
        first = today1.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = "December"
        year = "2022"
        total = payroll.pay_701 + payroll.pay_711 + payroll.rata
        return render(request, 'pds/payroll/show.html', {'pds':pds, 'payroll':payroll, 'month':month, 'year':year,'total':total})
    else:
        return redirect('/pds/view_payslip')



# HR Payslip
@login_required
def HRViewPayslip(request, id):
    if request.user.groups.filter(name='payroll'):
        sign = Signatory.objects.get(id= 2)
        pds = Personal.objects.filter(id=id).first()
        jan = Payslipstatus.objects.get(month='January')
        feb = Payslipstatus.objects.get(month='February')
        march = Payslipstatus.objects.get(month='March')
        april = Payslipstatus.objects.get(month='April')
        may = Payslipstatus.objects.get(month='May')
        june = Payslipstatus.objects.get(month='June')
        july = Payslipstatus.objects.get(month='July')
        aug = Payslipstatus.objects.get(month='August')
        sept = Payslipstatus.objects.get(month='September')
        octb = Payslipstatus.objects.get(month='October')
        nov = Payslipstatus.objects.get(month='November')
        dec = Payslipstatus.objects.get(month='December')
        context = { 'pds':pds ,'jan': jan, 'feb': feb, 'march': march, 'april': april, 'may': may, 'june': june, 'july': july, 'aug': aug, 'sept': sept, 'octb': octb, 'nov': nov, 'dec': dec,}
        return render(request, 'pds/payslip/view.html', context)
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/permanent')

@login_required
def HRViewJanuary(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = January.objects.filter(january_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1) 
                month = "January"
                year = "2023"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', { 'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewFebruary(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = February.objects.filter(february_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "February"
                year = "2023"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', { 'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewMarch(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = March.objects.filter(march_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "March"
                year = "2023"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', { 'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewApril(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = April.objects.filter(april_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "April"
                year = "2023"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', { 'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewMay(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = May.objects.filter(may_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "May"
                year = "2023"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', { 'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewJune(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = June.objects.filter(june_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "June"
                year = "2023"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', { 'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewJuly(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = July.objects.filter(july_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "July"
                year = "2023"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', { 'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewAugust(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = August.objects.filter(august_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "August"
                year = "2023"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', { 'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewSeptember(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = September.objects.filter(september_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "September"
                year = "2023"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', {'pds':pds,'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewOctober(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = October.objects.filter(october_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "October"
                year = "2022"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', {'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewNovember(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = November.objects.filter(november_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                bonus = Bonuses.objects.get(bonus_id=pds.author_id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "November"
                year = "2022"
                if bonus.tax:
                   bonusTax = bonus.tax
                else:     
                    bonusTax = 0
                if bonus.patcomc:
                   bonusPatcomc = bonus.patcomc
                else:     
                    bonusPatcomc = 0
                if bonus.liquidation:
                   bonusLiquidation = bonus.liquidation
                else:     
                    bonusLiquidation = 0

                total_yeb = bonus.year_end_bonus - bonusTax - bonusPatcomc - bonusLiquidation
                total_year_end_bonus = total_yeb + bonus.cash_gift
                total_nov = payroll.pay_701 + payroll.pay_711 
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata + bonus.year_end_bonus + bonus.cash_gift

                return render(request, 'pds/payslip/november.html', {'bonus':bonus, 'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total, 'total_year_end_bonus': total_year_end_bonus, 'total_nov': total_nov})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')

@login_required
def HRViewDecember(request, id):
    if request.user.groups.filter(name='payroll'):
        pds = Personal.objects.filter(id=id).first()
        payroll = December.objects.filter(december_id=pds.author_id).first()
        if payroll:
            
            if request.user.groups.filter(name='payroll'):
                pds = Personal.objects.get(id=id)
                sign = Signatory.objects.get(id= 2)
                today = datetime.datetime.now()
                today1 = datetime.date.today()
                first = today1.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                month = "December"
                year = "2022"
                total = payroll.pay_701 + payroll.pay_711 + payroll.rata
                return render(request, 'pds/payslip/show.html', { 'pds':pds, 'sign':sign,'payroll':payroll, 'month':month, 'year':year,'total':total})
            else:
                return redirect('/pds')
        else:
            pds = Personal.objects.filter(id=id).first()
            messages.success(request, 'Payslip not yet assigned to ' + str(pds.surname) + '.')
            return redirect('/pds/hr_view_payslip/' + str(pds.id) )
    else:
        return redirect('/pds/permanent')



@login_required 
def AANSOOPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='AANSOO').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ADMSPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='ADMS').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ANSPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='ANS').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ATSPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='ATS').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def CATCPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='CATC').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def CSISPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='CSIS').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ELSPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='ELS').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def FICGPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='FICG').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def FMDPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='FMD').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def FSISPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='FSIS').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def IASPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='IAS').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ODGPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='ODG').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def OFSAMPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='OFSAM').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required 
def ADMINPayslipNov(request):

    if request.user.groups.filter(name='payroll'):
        bonus = Bonuses.objects.filter(office='ADMIN').order_by('surname')
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

@login_required
def BonusesPage(request):
    if request.user.groups.filter(name='payroll'):
            
        bonus = Bonuses.objects.all()
        return render(request, 'pds/payslip/bonus.html', { 'bonus':bonus})
    else:
        return redirect('/pds/permanent')

# Edit November Payslipstatus
@login_required
def EditBonus(request, id):
    if request.user.groups.filter(name='payroll'):
            bonus = Bonuses.objects.get(id=id)
            form = BonusForm(request.POST, instance=bonus)
            if request.user.groups.filter(name='payroll'):
                if request.POST:
                    bonus = Bonuses.objects.get(id=id)
                    if form.is_valid():                                
                                instance = form.save(commit=False)
                                instance.id = id
                                instance.bonus_id = bonus.bonus_id
                                instance.edited_by = request.user.username
                                instance.save()
                                if request.POST['office'] == 'AANSOO':
                                    return redirect('/pds/aansoo_payroll_nov')
                                elif request.POST['office'] == 'ANS':
                                    return redirect('/pds/ans_payroll_nov')
                                elif request.POST['office'] == 'ADMS':
                                    return redirect('/pds/adms_payroll_nov')
                                elif request.POST['office'] == 'ATS':
                                    return redirect('/pds/ats_payroll_nov')
                                elif request.POST['office'] == 'CATC':
                                    return redirect('/pds/catc_payroll_nov')
                                elif request.POST['office'] == 'CSIS':
                                    return redirect('/pds/csis_payroll_nov')
                                elif request.POST['office'] == 'ELS':
                                    return redirect('/pds/els_payroll_nov')
                                elif request.POST['office'] == 'FICG':
                                    return redirect('/pds/ficg_payroll_nov')
                                elif request.POST['office'] == 'FMD':
                                    return redirect('/pds/fmd_payroll_nov')
                                elif request.POST['office'] == 'FSIS':
                                    return redirect('/pds/fsis_payroll_nov')
                                elif request.POST['office'] == 'IAS':
                                    return redirect('/pds/ias_payroll_nov')
                                elif request.POST['office'] == 'ODG':
                                    return redirect('/pds/odg_payroll_nov')
                                elif request.POST['office'] == 'OFSAM':
                                    return redirect('/pds/ofsam_payroll_nov')
                                elif request.POST['office'] == 'ADMIN':
                                    return redirect('/pds/admin_payroll_nov')
                                else:
                                    return redirect('/pds/bonuses')
                    context = {'bonus':bonus,'form':form }
                    return render(request,'pds/payslip/Edit_bonus.html', context)
                form = BonusForm(request.POST)
                return render(request,'pds/payslip/Edit_bonus.html', {'bonus':bonus, 'form':form})
            else:
                return HttpResponseRedirect(reverse('pds:index'))
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

# Edit November Payslipstatus
@login_required
def EditBonus2(request, id):
    if request.user.groups.filter(name='payroll'):
            bonus = Bonuses.objects.get(id=id)
            form = BonusForm(request.POST, instance=bonus)
            if request.user.groups.filter(name='payroll'):
                if request.POST:
                    bonus = Bonuses.objects.get(id=id)
                    if form.is_valid():                                
                                instance = form.save(commit=False)
                                instance.id = id
                                # instance.bonus_id = bonus.bonus_id
                                instance.edited_by = request.user.username
                                instance.save()
                                if request.POST['office'] == 'AANSOO':
                                    return redirect('/pds/aansoo_payroll_nov')
                                elif request.POST['office'] == 'ANS':
                                    return redirect('/pds/ans_payroll_nov')
                                elif request.POST['office'] == 'ADMS':
                                    return redirect('/pds/adms_payroll_nov')
                                elif request.POST['office'] == 'ATS':
                                    return redirect('/pds/ats_payroll_nov')
                                elif request.POST['office'] == 'CATC':
                                    return redirect('/pds/catc_payroll_nov')
                                elif request.POST['office'] == 'CSIS':
                                    return redirect('/pds/csis_payroll_nov')
                                elif request.POST['office'] == 'ELS':
                                    return redirect('/pds/els_payroll_nov')
                                elif request.POST['office'] == 'FICG':
                                    return redirect('/pds/ficg_payroll_nov')
                                elif request.POST['office'] == 'FD':
                                    return redirect('/pds/fmd_payroll_nov')
                                elif request.POST['office'] == 'FSIS':
                                    return redirect('/pds/fsis_payroll_nov')
                                elif request.POST['office'] == 'IAS':
                                    return redirect('/pds/ias_payroll_nov')
                                elif request.POST['office'] == 'ODG':
                                    return redirect('/pds/odg_payroll_nov')
                                elif request.POST['office'] == 'OFSAM':
                                    return redirect('/pds/ofsam_payroll_nov')
                                elif request.POST['office'] == 'ADMIN':
                                    return redirect('/pds/admin_payroll_nov')
                                else:
                                    return redirect('/pds/bonuses')
                    context = {'bonus':bonus,'form':form }
                    return render(request,'pds/payslip/Edit_bonus2.html', {'bonus':bonus, 'form':form})
                form = BonusForm(request.POST)
                return render(request,'pds/payslip/Edit_bonus2.html', {'bonus':bonus, 'form':form})
            else:
                return HttpResponseRedirect(reverse('pds:index'))
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def CreateBonus(request):
    if request.user.groups.filter(name='payroll'):
            if request.method == "POST":
                
                form = BonusForm(request.POST)
                if form.is_valid():
                        instance = form.save(commit=False)
                        instance.bonus_id = request.POST['bonus']
                        instance.edited_by = request.user.username
                        instance.save()
                        return redirect('/pds/bonuses')
            form = BonusForm(request.POST)
            return render(request,'pds/payslip/create_bonus.html',{'form':form})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

def CreateBonus2(request):
    if request.user.groups.filter(name='payroll'):
            if request.method == "POST":
                
                form = BonusForm(request.POST)
                if form.is_valid():
                        instance = form.save(commit=False)
                        # instance.bonus_id = request.POST['bonus']
                        instance.edited_by = request.user.username
                        instance.save()
                        return redirect('/pds/bonuses')
            form = BonusForm(request.POST)
            return render(request,'pds/payslip/create_bonus2.html',{'form':form})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds/hr')

