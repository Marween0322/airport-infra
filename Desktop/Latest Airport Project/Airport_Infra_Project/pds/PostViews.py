from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.views import generic 
from django.contrib import messages
from django.db.models import Q
import datetime

  
# Create your views here.
from .models import MultipleImage, Personal, Post, NotifyTraining
from .forms import PostForm, NotifyTrainingForm

@login_required
def Index(request):
    data = Post.objects.all().order_by('-post_date')

    users = User.objects.all()
        
    context = {'data': data, 'users':users}

    if request.user.groups.filter(name='hrmd'):
        return render(request, 'pds/post/index.html', context)
    else:
        return redirect('/pds')

@login_required
def Announcement(request):
    data = Post.objects.filter(status='Active').filter(post_type='Announcement').order_by('-post_date')

    context = {'data': data}
    return render(request, 'pds/announcements/index.html', context)

@login_required
def Reorg(request):
    data = Post.objects.filter(status='Active').filter(post_type='Reorg').order_by('-post_date')

    qna = Post.objects.filter(status='Active').filter(post_type='QnA').last()

    context = {'data': data, 'qna': qna}
    return render(request, 'pds/announcements/reorg.html', context)

@login_required
def QnA(request):
    data = Post.objects.filter(status='Active').filter(post_type='QnA').order_by('-post_date')

    context = {'data': data}
    return render(request, 'pds/announcements/qna.html', context)


@login_required
def PostCreate(request,*args,**kwargs):
    form = PostForm(request.POST,request.FILES)
    if request.FILES.get('upload'):
        file_check = 'True'
    else:
        file_check = 'False'  
    if request.user.groups.filter(name='hrmd'): 

            if request.POST:
                if form.is_valid():

                    instance = form.save(commit=False)
                    instance.create_by = request.user.username
                    instance.post_date = datetime.datetime.now()  
                    if file_check == 'True' :
                        instance.file = request.FILES['upload']  
                        extension = str(instance.file).split(".")[1].lower()
                        instance.ext = extension
                    instance.post_type = request.POST['post_type']
                    instance.status = 'Active'
                    instance.save()

                    images = request.FILES.getlist('images')
                    for image in images:
                        img = MultipleImage.objects.create(images=image)
                        img.post_id = instance.id
                        img.save()

                    return redirect('/pds/post')

                return render(request,'pds/post/create.html', {'form':form})
            return render(request,'pds/post/create.html', {'form':form})

    else:
        return redirect('/pds')

@login_required
def PostEdit(request, id):
    data = Post.objects.get(id=id)
   
    if request.user.groups.filter(name='hrmd'):   
        return render(request,'pds/post/edit.html', {'data':data})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required
def PostUpdate(request, id):
    if request.user.groups.filter(name='hrmd'):   
        data = Post.objects.get(id=id)
        form = PostForm(request.POST,request.FILES)
        if request.FILES.get('upload'):
            file_check = 'True'
        else:
            file_check = 'False'
        if request.POST:
            if form.is_valid():
                    data = Post.objects.get(id=id)
                    instance = form.save(commit=False)
                    instance.id = id
                    if file_check == 'True' :
                        instance.file = request.FILES['upload']   
                        extension = str(instance.file).split(".")[1].lower()
                        instance.ext = extension
                    else:
                        instance.file = data.file
                        if data.file == '':
                            pass
                        else:
                            extension = str(data.file).split(".")[1].lower()
                            instance.ext = extension
                    instance.status = request.POST['status']                    
                    instance.post_type = request.POST['post_type']
                    instance.create_by = data.create_by
                    instance.post_date = data.post_date
                    instance.save()

                    # Upload Images
                    images = request.FILES.getlist('images')
                    for image in images:
                        img = MultipleImage.objects.create(images=image)
                        img.post_id = instance.id
                        img.save()
                    return redirect('/pds/post')
            return render(request,'pds/post/edit.html', {'data':data})
    else:
        return render(request,'pds/post/edit.html', {'data':data})


@login_required
def NotifyTraining(request):
    pds = Personal.objects.filter(author=request.user).first()
    if pds.status == "Approved":
        if request.method == "POST":
            form = NotifyTrainingForm(request.POST)
            if form.is_valid():                
                form.save()
                instance = form.save(commit=False)
                instance.notify_id = pds.id
                instance.date_created = datetime.datetime.now()
                instance.save()
                messages.success(request, 'Your traings has been submitted for review, wait for approval.')
                return redirect('/pds/personalinfo3')
            else:
                messages.success(request, 'Submit error!.')
                return redirect('/pds/personalinfo3')
        return redirect('/pds/personalinfo3')
            
    else:
        return redirect('/pds')





