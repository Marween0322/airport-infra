from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.views import generic 
from django.contrib import messages
from django.db.models import Q
from django.views.static import serve
from django.utils.crypto import get_random_string
import datetime

# Create your views here.
from .models import Personal, Qrcode
from .forms import QrcodeForm


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    pds = Personal.objects.filter(author=request.user).first()
    if pds:
        if pds.status == "Approved":        
            return serve(request, path, document_root, show_indexes)
        else:
            return redirect('/pds')
    else:
        return redirect('/pds')



@login_required
def QRCode(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Central Office').exclude(status='INACTIVE').order_by('surname')[:100]
        office = "Central Office (100/Total)"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context)
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_ODG(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(service='Office of the Director General').exclude(status='INACTIVE').order_by('surname')
        office = "Office of the Director General"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')
    

def QR_ADMS(request):
    if request.user.groups.filter(name='qrcode'):    
        record = Personal.objects.filter(service='Aerodrome Development and Management Service').exclude(status='INACTIVE').order_by('surname')
        office = "Aerodrome Development and Management Service"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_ANS(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(service='Air Navigation Service').exclude(status='INACTIVE').order_by('surname')
        office = "Air Navigation Service"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

 
def QR_ATS(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(service='Air Traffic Service').exclude(status='INACTIVE').order_by('surname')
        office = "Air Traffic Service"
        context = {'record':record, 'office':office}
        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')
    

def QR_FSIS(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(service='Flight Standards Inspectorate Service').exclude(status='INACTIVE').order_by('surname')
        office = "Flight Standards Inspectorate Service"
        context = {'record':record, 'office':office}
        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')
    

def QR_AFS(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(service='Administrative and Finance Service').exclude(status='INACTIVE').order_by('surname')
        office = "Administrative and Finance Service"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')
def QRCode_all(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Central Office').exclude(status='INACTIVE').order_by('surname')
        office = "Central Office"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context)
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area1(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 01').exclude(status='INACTIVE').order_by('surname')
        office = "Area 01"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

# Area Centers
def QR_Area2(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 02').exclude(status='INACTIVE').order_by('surname')
        office = "Area 02"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area3(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 03').exclude(status='INACTIVE').order_by('surname')
        office = "Area 03"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area4(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 04').exclude(status='INACTIVE').order_by('surname')
        office = "Area 04"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area5(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 05').exclude(status='INACTIVE').order_by('surname')
        office = "Area 05"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area6(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 06').exclude(status='INACTIVE').order_by('surname')
        office = "Area 06"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area7(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 07').exclude(status='INACTIVE').order_by('surname')
        office = "Area 07"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area8(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 08').exclude(status='INACTIVE').order_by('surname')
        office = "Area 08"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area9(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 09').exclude(status='INACTIVE').order_by('surname')
        office = "Area 09"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area10(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 10').exclude(status='INACTIVE').order_by('surname')
        office = "Area 10"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area11(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 12').exclude(status='INACTIVE').order_by('surname')
        office = "Area 11"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')

def QR_Area12(request):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.filter(assignment__iexact='Area 12').exclude(status='INACTIVE').order_by('surname')
        office = "Area 12"
        context = {'record':record, 'office':office}

        return render(request, 'caapid/index.html', context) 
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')
    



# QR COde
@login_required
def AddQR(request, id):
    if request.user.groups.filter(name='qrcode'):
        record = Personal.objects.get(id=id)
        random = get_random_string(length=6).upper()

        if request.method == "POST":

                    form = QrcodeForm(request.POST)
            
                    form.save()
                    instance = form.save(commit=False)
                    instance.qr_id = record.id
                    instance.url_name = 'portal.caap.gov.ph/caapid/show/' + random
                    instance.unique_id = random
                    instance.emp_name = record.surname + record.first_name
                    instance.save()
                    # Always return an HttpResponseRedirect after successfully dealing
                    # with POST data. This prevents data from being posted twice if a
                    # user hits the Back button.
                    messages.success(request, 'QR Code Generated for ... '  + str(instance.emp_name) +"'" + '.')
                    return redirect('/pds/qrcode')
        form = QrcodeForm(request.POST)        
        return render(request, 'dts/records/qr.html',{'form':form, 'id':id})
    else:
       messages.success(request, 'Unauthorized Access')
       return redirect('/pds/hr')
    

def QR_Show(request, id):
    qr = Qrcode.objects.get(unique_id__iexact=id)
    record = Personal.objects.filter(id=qr.qr_id).exclude(status='INACTIVE').order_by('surname').first()
    return render(request, 'caapid/show.html',{'record':record}) 
