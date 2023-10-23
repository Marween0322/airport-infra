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

#import from PDS models
from pds.models import Personal
# Bulletin Models
from .models import Bulletin, BulletinFile, Aknowledge, BulletinComment
from .forms import BulletinForm, BulletinCommentForm

# Create your views here.

# Image for Authenticated Users only
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

# Bulletin Board For Management
@login_required
def BulletinHome(request): 
    data = Bulletin.objects.all().order_by('-id')[:15]
    
    context = {'data': data}    

    if request.user.groups.filter(name='memo'):
        return render(request, 'dashboard/index.html', context)
    else:
        return redirect('/pds')

   
@login_required
def BulletinCreate(request,*args,**kwargs): 
    form = BulletinForm(request.POST,request.FILES)
    if request.FILES.get('upload'):
        file_check = 'True'
    else:
        file_check = 'False'  
    if request.user.groups.filter(name='odg'): 

            if request.POST:
                if form.is_valid():

                    instance = form.save(commit=False)
                    instance.create_by = request.user.first_name + ', ' + request.user.last_name
                    instance.bulletin_date = datetime.now()                      
                    instance.status = 'Active'
                    instance.save()

                    images = request.FILES.getlist('files')
                    for image in images:
                        img = BulletinFile.objects.create(images=image)
                        img.bulletin_id = instance.id
                        img.upload_date = datetime.now()                           
                        extension = str(img.images).split(".")[1].lower()
                        img.ext = extension
                        img.save()

                    return redirect('/dashboard/bulletin')

                return render(request,'dashboard/bulletin/create.html', {'form':form})
            return render(request,'dashboard/bulletin/create.html', {'form':form})

    else:
        return redirect('/dashboard/')

@login_required
def Bulletin_Aknldg(request, id): 
    
    # Get Bulletin Details
    bulletin = Bulletin.objects.get(id=id)

    # Aknowledge Bulletin Post
    Aknwldg = Aknowledge.objects.create(
        bulletin_title = bulletin.subject,
        bulletin_id = bulletin.id,
        aknowledge_date = datetime.now(),
        status = "Aknowledge",
        create_by = request.user.first_name + ", " +request.user.last_name,        
        create_by_id = request.user.id,
        )
    return redirect('/dashboard/bulletin')

@login_required
def Bulletin_Comment(request, id): 
    
    # Get Bulletin Details
    bulletin = Bulletin.objects.get(id=id)

    # Aknowledge Bulletin Post
    commnt = BulletinComment.objects.create(
        comment = request.POST['comment'],
        bulletin_id = bulletin.id,
        comment_date = datetime.now(),
        create_by = request.user.first_name + ", " +request.user.last_name, 
        )
    return redirect('/dashboard/bulletin')

@login_required
def Acknowledge(request): 
    
    # Get Bulletin Details
    bulletins = Bulletin.objects.all()
    
    if request.user.groups.filter(name='memo'):
        return render(request, 'dashboard/bulletin/acknowledge.html', {'bulletins': bulletins})
    else:
        return redirect('/pds')

@login_required
def Bulletin_Post(request, id): 
    
    bulletin = Bulletin.objects.get(id=id)
    
    context = {'bulletin': bulletin}
    
    if request.user.groups.filter(name='memo'):
        return render(request, 'dashboard/bulletin/index.html', context)
    else:
        return redirect('/pds')

