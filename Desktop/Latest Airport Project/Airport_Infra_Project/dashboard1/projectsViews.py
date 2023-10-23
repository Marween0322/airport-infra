from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.views import generic 
from django.contrib import messages
from django.db.models import Q
from django.views.static import serve
from datetime import datetime, timezone, date
from django.db.models import Sum
from decimal import Decimal

from .models import AiportProject
from .forms import AiportProjectForm
from django.views.decorators.clickjacking import xframe_options_exempt



@login_required
def addProject(request):   
    if request.user.groups.filter(name='adms'):
        if request.method == "POST":    
            form = AiportProjectForm(request.POST) 
            if form.is_valid():
                today = datetime.now()
                instance = form.save(commit=False)
                instance.created_by = f"{request.user.first_name} {request.user.last_name}"
                instance.date_created = today

                # Ensure fund_amount is not None
                fund_amount = form.cleaned_data.get('fund_amount')

                if fund_amount is not None and fund_amount.strip() != "":
                    instance.fund_amount = str(fund_amount)
                else:
                    instance.fund_amount = "00.0"

                # Ensure contract_amount is not None
                contract_amount = form.cleaned_data.get('contract_amount')

                if contract_amount is not None and contract_amount.strip() != "":
                    instance.contract_amount = str(contract_amount)
                else:
                    instance.contract_amount = "00.0"

                instance.save()

                if instance.agency == "CAAP":
                    return redirect('/dashboard/caap')
                else:
                    return redirect('/dashboard/dotr')
            else:
                print(form)
                print("Invalid Form")
                print(form.errors)
                messages.success(request, 'Submit error!.')
                return render(request, 'dashboard/projects/add_record.html', {'form': form})

        form = AiportProjectForm(request.POST)
        return render(request, 'dashboard/projects/add_record.html', {'form': form})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')
    

@login_required 
def CAAP(request):
    projects = AiportProject.objects.filter(agency="CAAP").order_by('title')
    name = "CAAP"

    if request.user.groups.filter(name='odg'):
        return render(request,"dashboard/projects/project_table.html",{'projects':projects , 'name':name}) 
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')     

@login_required 
def DOTr(request):
    projects = AiportProject.objects.filter(agency="DOTr").order_by('title')
    name = "DOTr"

    if request.user.groups.filter(name='odg'):
        return render(request,"dashboard/projects/project_table.html",{'projects':projects , 'name':name}) 
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds') 

@login_required 
def edit(request, id):  
    project = AiportProject.objects.get(id=id)  

    if request.user.groups.filter(name='adms'):
        return render(request,'dashboard/projects/edit.html', {'project':project })   
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')

@login_required 
def show_project(request, id): 
    context ={}

    context["project"] = AiportProject.objects.get(id = id)

    if request.user.groups.filter(name='odg'):
        return render(request, "dashboard/projects/show_project.html", context)
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')        
    

@login_required 
def update(request, id):  

    if request.user.groups.filter(name='adms'):
        if request.POST:
                today = datetime.now()
                project = AiportProject.objects.get(id=id)
                form = AiportProjectForm(request.POST)
                
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.id = id
                    instance.edited_by = request.user.first_name + " " + request.user.first_name
                    instance.date_edited = today
                    instance.save()
                    if project.agency == "CAAP":
                        return redirect('/dashboard/caap')
                    else:
                        return redirect('/dashboard/dotr')
                else:
                    print(form)
                    print("Invalid Form")
                    print(form.errors)
                    return render(request,'dashboard/projects/edit.html',  {'project':project,'form':form})
                
                return render(request,'dashboard/projects/edit.html',  {'project':project})
        return redirect('/dashboard/caap')
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')

    

@login_required 
def destroy(request, id):       

    if request.user.groups.filter(name='adms'):
        aproj = AiportProject.objects.get(id=id)  
        aproj.delete()  
        if project.agency == "CAAP":
            return redirect('/dashboard/caap')
        else:
            return redirect('/dashboard/dotr')
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')


@login_required 
def viewProject(request,id): 

    view_proj = AiportProject.objects.get(id = id)

    if request.user.groups.filter(name='odg'):
        return render(request,'dashboard/projects/view.html', {'view' : view_proj })
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')
    
    

@login_required 
def dashView(request):
    if request.user.groups.filter(name='odg'):
        datetoday = datetime.now()
        year = datetoday.strftime('%Y')
        last_year = int(year) - 1
        last_2year = int(year) - 2
        last_3year = int(year) - 3
        last_4year = int(year) - 4
        last_5year = int(year) - 5
        last_6year = int(year) - 6
        last_7year = int(year) - 7
        last_8year = int(year) - 8


        projects = AiportProject.objects.all()[:300] 
        count_all = AiportProject.objects.all().count()
        count_dotr = AiportProject.objects.filter(agency__icontains="DOTR").count()
        count_caap = AiportProject.objects.filter(agency__icontains="CAAP").count()
        count_complete = AiportProject.objects.filter(status="Completed").count()
        count_ongoing = AiportProject.objects.filter(status="On- going").count()
        count_procurement = AiportProject.objects.filter(status="under procurement").count()    
        count_detailed = AiportProject.objects.filter(status="DED").count()
        count_acquisition = AiportProject.objects.filter(status="SAC").count()

        # Filter This Year
        caap_all = AiportProject.objects.filter(agency="CAAP").count()
        dotr_all = AiportProject.objects.filter(agency="DOTr").count()

        caap_complete = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").count()
        caap_ongoing = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").count()
        caap_procurement = AiportProject.objects.filter(status="Under Procurement").filter(agency="CAAP").count()
        caap_processing  = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="CAAP").count()
        caap_detailed = AiportProject.objects.filter(status="DED").filter(agency="CAAP").count()
        caap_acquisition = AiportProject.objects.filter(status="SAC").filter(agency="CAAP").count()
        caap_Others = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="CAAP").count()
        dotr_complete = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").count()
        dotr_ongoing = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").count()
        dotr_procurement = AiportProject.objects.filter(status="Under Procurement").filter(agency="DOTr").count()
        dotr_processing  = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="DOTr").count()
        dotr_detailed = AiportProject.objects.filter(status="DED").filter(agency="DOTr").count()
        dotr_acquisition = AiportProject.objects.filter(status="SAC").filter(agency="DOTr").count()
        dotr_Others = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="DOTr").count()
        # Filter Last Year
        caap_complete1 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=last_year).count()
        caap_ongoing1 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=last_year).count()
        caap_procurement1 = AiportProject.objects.filter(status="Under Procurement").filter(agency="CAAP").filter(fund_year=last_year).count()
        caap_processing1  = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="CAAP").filter(fund_year=last_year).count()
        caap_detailed1 = AiportProject.objects.filter(status="DED").filter(agency="CAAP").filter(fund_year=last_year).count()
        caap_acquisition1 = AiportProject.objects.filter(status="SAC").filter(agency="CAAP").filter(fund_year=last_year).count()
        caap_Others1 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="CAAP").filter(fund_year=last_year).count()
        dotr_complete1 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=last_year).count()
        dotr_ongoing1 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=last_year).count()
        dotr_procurement1 = AiportProject.objects.filter(status="Under Procurement").filter(agency="DOTr").filter(fund_year=last_year).count()
        dotr_processing1  = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="DOTr").filter(fund_year=last_year).count()
        dotr_detailed1 = AiportProject.objects.filter(status="DED").filter(agency="DOTr").filter(fund_year=last_year).count()
        dotr_acquisition1 = AiportProject.objects.filter(status="SAC").filter(agency="DOTr").filter(fund_year=last_year).count()
        dotr_Others1 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="DOTr").filter(fund_year=last_year).count()
        # Filter past 2 Year
        caap_complete2 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        caap_ongoing2 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        caap_procurement2 = AiportProject.objects.filter(status="Under Procurement").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        caap_processing2 = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        caap_detailed2 = AiportProject.objects.filter(status="DED").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        caap_acquisition2 = AiportProject.objects.filter(status="SAC").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        caap_Others2 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        dotr_complete2 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        dotr_ongoing2 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        dotr_procurement2 = AiportProject.objects.filter(status="Under Procurement").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        dotr_processing2 = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        dotr_detailed2 = AiportProject.objects.filter(status="DED").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        dotr_acquisition2 = AiportProject.objects.filter(status="SAC").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        dotr_Others2 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).count()
        # Filter Past 3 year
        caap_complete3 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        caap_ongoing3 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        caap_procurement3 = AiportProject.objects.filter(status="Under Procurement").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        caap_processing3 = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        caap_detailed3 = AiportProject.objects.filter(status="DED").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        caap_acquisition3 = AiportProject.objects.filter(status="SAC").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        caap_Others3 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        dotr_complete3 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        dotr_ongoing3 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        dotr_procurement3 = AiportProject.objects.filter(status="Under Procurement").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        dotr_processing3 = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        dotr_detailed3 = AiportProject.objects.filter(status="DED").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        dotr_acquisition3 = AiportProject.objects.filter(status="SAC").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()
        dotr_Others3 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).count()

        # Filter This Year Sum Amount
        caap_complete_sum = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_ongoing_sum = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_procurement_sum = AiportProject.objects.filter(status="Under Procurement").filter(agency="CAAP").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_processing_sum = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="CAAP").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_detailed_sum = AiportProject.objects.filter(status="DED").filter(agency="CAAP").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_acquisition_sum = AiportProject.objects.filter(status="SAC").filter(agency="CAAP").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_Others_sum = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="CAAP").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_complete_sum = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_ongoing_sum = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_procurement_sum = AiportProject.objects.filter(status="Under Procurement").filter(agency="DOTr").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_processing_sum = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="DOTr").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_detailed_sum = AiportProject.objects.filter(status="DED").filter(agency="DOTr").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_acquisition_sum = AiportProject.objects.filter(status="SAC").filter(agency="DOTr").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_Others_sum = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="DOTr").values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        # Filter Last Year Sum Amount
        caap_complete_sum1 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_ongoing_sum1 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_procurement_sum1 = AiportProject.objects.filter(status="Under Procurement").filter(agency="CAAP").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_processing_sum1  = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="CAAP").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_detailed_sum1 = AiportProject.objects.filter(status="DED").filter(agency="CAAP").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_acquisition_sum1 = AiportProject.objects.filter(status="SAC").filter(agency="CAAP").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_Others_sum1 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="CAAP").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_complete_sum1 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_ongoing_sum1 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_procurement_sum1 = AiportProject.objects.filter(status="Under Procurement").filter(agency="DOTr").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_processing_sum1  = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="DOTr").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_detailed_sum1 = AiportProject.objects.filter(status="DED").filter(agency="DOTr").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_acquisition_sum1 = AiportProject.objects.filter(status="SAC").filter(agency="DOTr").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_Others_sum1 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="DOTr").filter(fund_year=last_year).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        # Filter past 2 Year Sum Amount
        caap_complete_sum2 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_ongoing_sum2 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_procurement_sum2 = AiportProject.objects.filter(status="Under Procurement").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_processing_sum2 = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_detailed_sum2 = AiportProject.objects.filter(status="DED").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_acquisition_sum2 = AiportProject.objects.filter(status="SAC").filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_Others_sum2 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="CAAP").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_complete_sum2 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_ongoing_sum2 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_procurement_sum2 = AiportProject.objects.filter(status="Under Procurement").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_processing_sum2 = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_detailed_sum2 = AiportProject.objects.filter(status="DED").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_acquisition_sum2 = AiportProject.objects.filter(status="SAC").filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_Others_sum2 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="DOTr").filter(Q(fund_year=last_2year) | Q(fund_year=last_3year) | Q(fund_year=last_4year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        # Filter Past 3 year Sum Amount
        caap_complete_sum3 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_ongoing_sum3 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_procurement_sum3 = AiportProject.objects.filter(status="Under Procurement").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_processing_sum3 = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_detailed_sum3 = AiportProject.objects.filter(status="DED").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_acquisition_sum3 = AiportProject.objects.filter(status="SAC").filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        caap_Others_sum3 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="CAAP").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_complete_sum3 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_ongoing_sum3 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_procurement_sum3 = AiportProject.objects.filter(status="Under Procurement").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_processing_sum3 = AiportProject.objects.filter(status="Processing of POW & Plans").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_detailed_sum3 = AiportProject.objects.filter(status="DED").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_acquisition_sum3 = AiportProject.objects.filter(status="SAC").filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        dotr_Others_sum3 = AiportProject.objects.filter( Q(status="Others") | Q(status="Others/Budget donated") | Q(status="Others/for deduction") | Q(status="Others/Forwarded") | Q(status="Others/MOA") | Q(status="Others/On- hold")).filter(agency="DOTr").filter(Q(fund_year=last_5year) | Q(fund_year=last_6year) | Q(fund_year=last_7year)| Q(fund_year=last_8year)).values('contract_amount').aggregate(Sum('contract_amount')).get('contract_amount__sum', 0.00)
        # Get Percentage
        caap_complete_percnt = (caap_complete/caap_all) * 100
        caap_ongoing_percnt = (caap_ongoing/caap_all) * 100
        caap_detailed_percnt = (caap_detailed/caap_all) * 100
        caap_acquisition_percnt = (caap_acquisition/caap_all) * 100
        dotr_complete_percnt = (dotr_complete/dotr_all) * 100
        dotr_ongoing_percnt = (dotr_ongoing/dotr_all) * 100
        dotr_detailed_percnt = (dotr_detailed/dotr_all) * 100
        dotr_acquisition_percnt = (dotr_acquisition/dotr_all) * 100

        count_complete_percnt = (count_complete/count_all) * 100
        count_ongoing_percnt = (count_ongoing/count_all) * 100
        count_detailed_percnt = (count_detailed/count_all) * 100
        count_acquisition_percnt = (count_acquisition/count_all) * 100

        caap_complete_bar = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=year).count()
        caap_complete_bar1 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=last_year).count()
        caap_complete_bar2 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=last_2year).count()
        caap_complete_bar3 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=last_3year).count()
        caap_complete_bar4 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=last_4year).count()    
        caap_complete_bar5 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=last_5year).count()
        caap_complete_bar6 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=last_6year).count()
        caap_complete_bar7 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=last_7year).count()
        caap_complete_bar8 = AiportProject.objects.filter(status="Completed").filter(agency="CAAP").filter(fund_year=last_8year).count()

        dotr_complete_bar = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=year).count()
        dotr_complete_bar1 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=last_year).count()
        dotr_complete_bar2 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=last_2year).count()
        dotr_complete_bar3 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=last_3year).count()
        dotr_complete_bar4 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=last_4year).count()
        dotr_complete_bar5 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=last_5year).count()
        dotr_complete_bar6 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=last_6year).count()
        dotr_complete_bar7 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=last_7year).count()
        dotr_complete_bar8 = AiportProject.objects.filter(status="Completed").filter(agency="DOTr").filter(fund_year=last_8year).count()

        caap_ongoing_bar = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=year).count()
        caap_ongoing_bar1 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=last_year).count()
        caap_ongoing_bar2 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=last_2year).count()
        caap_ongoing_bar3 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=last_3year).count()
        caap_ongoing_bar4 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=last_4year).count()    
        caap_ongoing_bar5 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=last_5year).count()
        caap_ongoing_bar6 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=last_6year).count()
        caap_ongoing_bar7 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=last_7year).count()
        caap_ongoing_bar8 = AiportProject.objects.filter(status="On- going").filter(agency="CAAP").filter(fund_year=last_8year).count()

        dotr_ongoing_bar = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=year).count()
        dotr_ongoing_bar1 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=last_year).count()
        dotr_ongoing_bar2 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=last_2year).count()
        dotr_ongoing_bar3 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=last_3year).count()
        dotr_ongoing_bar4 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=last_4year).count()
        dotr_ongoing_bar5 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=last_5year).count()
        dotr_ongoing_bar6 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=last_6year).count()
        dotr_ongoing_bar7 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=last_7year).count()
        dotr_ongoing_bar8 = AiportProject.objects.filter(status="On- going").filter(agency="DOTr").filter(fund_year=last_8year).count()


        context = {'year':year,'last_year':last_year,'last_2year':last_2year,'last_3year':last_3year,'last_4year':last_4year,'last_5year':last_5year,'last_6year':last_6year,'last_7year':last_7year,'last_8year':last_8year, 'projects':projects, 'count_caap':count_caap, 'count_dotr':count_dotr, 'count_complete':count_complete, 'count_ongoing':count_ongoing, 'count_detailed':count_detailed, 'count_acquisition':count_acquisition, 'count_procurement':count_procurement, 'caap_complete': caap_complete, 'caap_ongoing': caap_ongoing, 'caap_procurement': caap_procurement, 'caap_processing': caap_processing, 'caap_detailed': caap_detailed, 'caap_acquisition': caap_acquisition, 'caap_Others': caap_Others,    'dotr_complete': dotr_complete, 'dotr_ongoing': dotr_ongoing, 'dotr_procurement': dotr_procurement, 'dotr_processing': dotr_processing, 'dotr_detailed': dotr_detailed, 'dotr_acquisition': dotr_acquisition, 'dotr_Others': dotr_Others ,'caap_complete1': caap_complete1, 'caap_ongoing1': caap_ongoing1, 'caap_procurement1': caap_procurement1, 'caap_processing1': caap_processing1, 'caap_detailed1': caap_detailed1, 'caap_acquisition1': caap_acquisition1, 'caap_Others1': caap_Others,'dotr_complete1': dotr_complete1, 'dotr_ongoing1': dotr_ongoing1, 'dotr_procurement1': dotr_procurement1, 'dotr_processing1': dotr_processing1, 'dotr_detailed1': dotr_detailed1, 'dotr_acquisition1': dotr_acquisition1, 'dotr_Others1': dotr_Others1 ,'caap_complete2': caap_complete2, 'caap_ongoing2': caap_ongoing2, 'caap_procurement2': caap_procurement2, 'caap_processing2': caap_processing2, 'caap_detailed2': caap_detailed2, 'caap_acquisition2': caap_acquisition2, 'caap_Others2': caap_Others,'dotr_complete2': dotr_complete2, 'dotr_ongoing2': dotr_ongoing2, 'dotr_procurement2': dotr_procurement2, 'dotr_processing2': dotr_processing2, 'dotr_detailed2': dotr_detailed2, 'dotr_acquisition2': dotr_acquisition2, 'dotr_Others2': dotr_Others2 ,'caap_complete3': caap_complete3, 'caap_ongoing3': caap_ongoing3, 'caap_procurement3': caap_procurement3, 'caap_processing3': caap_processing3, 'caap_detailed3': caap_detailed3, 'caap_acquisition3': caap_acquisition3, 'caap_Others3': caap_Others,'dotr_complete3': dotr_complete3, 'dotr_ongoing3': dotr_ongoing3, 'dotr_procurement3': dotr_procurement3, 'dotr_processing3': dotr_processing3, 'dotr_detailed3': dotr_detailed3, 'dotr_acquisition3': dotr_acquisition3, 'dotr_Others3': dotr_Others3,'caap_complete_sum': caap_complete_sum, 'caap_ongoing_sum': caap_ongoing_sum, 'caap_procurement_sum': caap_procurement_sum, 'caap_processing_sum': caap_processing_sum, 'caap_detailed_sum': caap_detailed_sum, 'caap_acquisition_sum': caap_acquisition_sum, 'caap_Others_sum': caap_Others,'dotr_complete_sum': dotr_complete_sum, 'dotr_ongoing_sum': dotr_ongoing_sum, 'dotr_procurement_sum': dotr_procurement_sum, 'dotr_processing_sum': dotr_processing_sum, 'dotr_detailed_sum': dotr_detailed_sum, 'dotr_acquisition_sum': dotr_acquisition_sum, 'dotr_Others_sum': dotr_Others_sum ,'caap_complete_sum1': caap_complete_sum1, 'caap_ongoing_sum1': caap_ongoing_sum1, 'caap_procurement_sum1': caap_procurement_sum1, 'caap_processing_sum1': caap_processing_sum1, 'caap_detailed_sum1': caap_detailed_sum1, 'caap_acquisition_sum1': caap_acquisition_sum1, 'caap_Others_sum1': caap_Others,'dotr_complete_sum1': dotr_complete_sum1, 'dotr_ongoing_sum1': dotr_ongoing_sum1, 'dotr_procurement_sum1': dotr_procurement_sum1, 'dotr_processing_sum1': dotr_processing_sum1, 'dotr_detailed_sum1': dotr_detailed_sum1, 'dotr_acquisition_sum1': dotr_acquisition_sum1, 'dotr_Others_sum1': dotr_Others_sum1 ,'caap_complete_sum2': caap_complete_sum2, 'caap_ongoing_sum2': caap_ongoing_sum2, 'caap_procurement_sum2': caap_procurement_sum2, 'caap_processing_sum2': caap_processing_sum2, 'caap_detailed_sum2': caap_detailed_sum2, 'caap_acquisition_sum2': caap_acquisition_sum2, 'caap_Others_sum2': caap_Others,'dotr_complete_sum2': dotr_complete_sum2, 'dotr_ongoing_sum2': dotr_ongoing_sum2, 'dotr_procurement_sum2': dotr_procurement_sum2, 'dotr_processing_sum2': dotr_processing_sum2, 'dotr_detailed_sum2': dotr_detailed_sum2, 'dotr_acquisition_sum2': dotr_acquisition_sum2, 'dotr_Others_sum2': dotr_Others_sum2 ,'caap_complete_sum3': caap_complete_sum3, 'caap_ongoing_sum3': caap_ongoing_sum3, 'caap_procurement_sum3': caap_procurement_sum3, 'caap_processing_sum3': caap_processing_sum3, 'caap_detailed_sum3': caap_detailed_sum3, 'caap_acquisition_sum3': caap_acquisition_sum3, 'caap_Others_sum3': caap_Others,'dotr_complete_sum3': dotr_complete_sum3, 'dotr_ongoing_sum3': dotr_ongoing_sum3, 'dotr_procurement_sum3': dotr_procurement_sum3, 'dotr_processing_sum3': dotr_processing_sum3, 'dotr_detailed_sum3': dotr_detailed_sum3, 'dotr_acquisition_sum3': dotr_acquisition_sum3, 'dotr_Others_sum3': dotr_Others_sum3 ,'caap_complete_sum1': caap_complete_sum1, 'caap_ongoing_sum1': caap_ongoing_sum1, 'caap_procurement_sum1': caap_procurement_sum1, 'caap_processing_sum1': caap_processing_sum1, 'caap_detailed_sum1': caap_detailed_sum1, 'caap_acquisition_sum1': caap_acquisition_sum1, 'caap_Others_sum1': caap_Others,'caap_complete_sum1': caap_complete_sum1, 'caap_ongoing_sum1': caap_ongoing_sum1, 'caap_procurement_sum1': caap_procurement_sum1, 'caap_processing_sum1': caap_processing_sum1, 'caap_detailed_sum1': caap_detailed_sum1, 'caap_acquisition_sum1': caap_acquisition_sum1, 'caap_Others_sum1':caap_Others_sum1 ,'caap_complete_sum2': caap_complete_sum2, 'caap_ongoing_sum2': caap_ongoing_sum2, 'caap_procurement_sum2': caap_procurement_sum2, 'caap_processing_sum2': caap_processing_sum2, 'caap_detailed_sum2': caap_detailed_sum2, 'caap_acquisition_sum2': caap_acquisition_sum2, 'caap_Others_sum2': caap_Others,'caap_complete_sum2': caap_complete_sum2, 'caap_ongoing_sum2': caap_ongoing_sum2, 'caap_procurement_sum2': caap_procurement_sum2, 'caap_processing_sum2': caap_processing_sum2, 'caap_detailed_sum2': caap_detailed_sum2, 'caap_acquisition_sum2': caap_acquisition_sum2, 'caap_Others_sum2':caap_Others_sum2 ,'caap_complete_sum3': caap_complete_sum3, 'caap_ongoing_sum3': caap_ongoing_sum3, 'caap_procurement_sum3': caap_procurement_sum3, 'caap_processing_sum3': caap_processing_sum3, 'caap_detailed_sum3': caap_detailed_sum3, 'caap_acquisition_sum3': caap_acquisition_sum3, 'caap_Others_sum3': caap_Others,'caap_complete_sum3': caap_complete_sum3, 'caap_ongoing_sum3': caap_ongoing_sum3, 'caap_procurement_sum3': caap_procurement_sum3, 'caap_processing_sum3': caap_processing_sum3, 'caap_detailed_sum3': caap_detailed_sum3, 'caap_acquisition_sum3': caap_acquisition_sum3, 'caap_Others_sum3':caap_Others_sum3 ,'caap_complete_sum': caap_complete_sum, 'caap_ongoing_sum': caap_ongoing_sum, 'caap_procurement_sum': caap_procurement_sum, 'caap_processing_sum': caap_processing_sum, 'caap_detailed_sum': caap_detailed_sum, 'caap_acquisition_sum': caap_acquisition_sum, 'caap_Others_sum': caap_Others,'caap_complete_sum': caap_complete_sum, 'caap_ongoing_sum': caap_ongoing_sum, 'caap_procurement_sum': caap_procurement_sum, 'caap_processing_sum': caap_processing_sum, 'caap_detailed_sum': caap_detailed_sum, 'caap_acquisition_sum': caap_acquisition_sum, 'caap_Others_sum':caap_Others_sum ,'caap_complete_percnt': caap_complete_percnt ,'caap_ongoing_percnt': caap_ongoing_percnt ,'caap_detailed_percnt': caap_detailed_percnt ,'caap_acquisition_percnt': caap_acquisition_percnt,'dotr_complete_percnt': dotr_complete_percnt ,'dotr_ongoing_percnt': dotr_ongoing_percnt ,'dotr_detailed_percnt': dotr_detailed_percnt ,'dotr_acquisition_percnt': dotr_acquisition_percnt ,'count_complete_percnt': count_complete_percnt ,'count_ongoing_percnt': count_ongoing_percnt ,'count_detailed_percnt': count_detailed_percnt ,'count_acquisition_percnt': count_acquisition_percnt , 'caap_complete_bar': caap_complete_bar , 'caap_complete_bar1' : caap_complete_bar1 , 'caap_complete_bar2' : caap_complete_bar2 , 'caap_complete_bar3' : caap_complete_bar3 , 'caap_complete_bar4' : caap_complete_bar4 , 'caap_complete_bar5' : caap_complete_bar5 , 'caap_complete_bar6' : caap_complete_bar6, 'caap_complete_bar7' : caap_complete_bar7, 'caap_complete_bar8' : caap_complete_bar8, 'dotr_complete_bar': dotr_complete_bar , 'dotr_complete_bar1' : dotr_complete_bar1 , 'dotr_complete_bar2' : dotr_complete_bar2 , 'dotr_complete_bar3' : dotr_complete_bar3 , 'dotr_complete_bar4' : dotr_complete_bar4 , 'dotr_complete_bar5' : dotr_complete_bar5 , 'dotr_complete_bar6' : dotr_complete_bar6, 'dotr_complete_bar7' : dotr_complete_bar7, 'dotr_complete_bar8' : dotr_complete_bar8 , 'caap_ongoing_bar': caap_ongoing_bar , 'caap_ongoing_bar1' : caap_ongoing_bar1 , 'caap_ongoing_bar2' : caap_ongoing_bar2 , 'caap_ongoing_bar3' : caap_ongoing_bar3 , 'caap_ongoing_bar4' : caap_ongoing_bar4 , 'caap_ongoing_bar5' : caap_ongoing_bar5 , 'caap_ongoing_bar6' : caap_ongoing_bar6, 'caap_ongoing_bar7' : caap_ongoing_bar7, 'caap_ongoing_bar8' : caap_ongoing_bar8, 'dotr_ongoing_bar': dotr_ongoing_bar , 'dotr_ongoing_bar1' : dotr_ongoing_bar1 , 'dotr_ongoing_bar2' : dotr_ongoing_bar2 , 'dotr_ongoing_bar3' : dotr_ongoing_bar3 , 'dotr_ongoing_bar4' : dotr_ongoing_bar4 , 'dotr_ongoing_bar5' : dotr_ongoing_bar5 , 'dotr_ongoing_bar6' : dotr_ongoing_bar6, 'dotr_ongoing_bar7' : dotr_ongoing_bar7, 'dotr_ongoing_bar8' : dotr_ongoing_bar8 }
        return render(request,"dashboard/projects/dashboard.html", context)
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')    

@login_required 
def Project(request, name):    
    projects = AiportProject.objects.filter(location__icontains= name).order_by('title')

    if request.user.groups.filter(name='odg'):
        return render(request,'dashboard/projects/projects.html', {'projects': projects, 'name': name})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')    

@login_required 
def complete_projects(request):
    projects = AiportProject.objects.filter(status="Completed").order_by('title')
    name = "Completed"

    if request.user.groups.filter(name='odg'):
        return render(request,'dashboard/projects/projects.html', {'projects': projects, 'name': name})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds') 

@login_required 
def ongoing_projects(request):
    projects = AiportProject.objects.filter(status="On- going").order_by('title')
    name = "On-Going"

    if request.user.groups.filter(name='odg'):
        return render(request,'dashboard/projects/projects.html', {'projects': projects, 'name': name})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')  

@login_required 
def procurement_projects(request):
    projects = AiportProject.objects.filter(status="under procurement").order_by('title')
    name = "Under Procurement"

    if request.user.groups.filter(name='odg'):
        return render(request,'dashboard/projects/projects.html', {'projects': projects, 'name': name})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')  


@login_required
def SearchProject(request):
    value_project = request.POST['search_project']    
    value_agency = request.POST['search_agency']      
    value_order = request.POST['search_order']
    
    projects = AiportProject.objects.filter(agency=value_agency).filter(Q(title__icontains=value_project)|Q(location__icontains=value_project)|Q(contract_contractor__icontains=value_project)).order_by(value_order)
    context = {'projects': projects}
    name = request.POST['search_agency']
    if request.user.groups.filter(name='odg'):
        return render(request,"dashboard/projects/project_table.html",{'projects':projects , 'name':name, 'value_project':value_project}) 
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')  






