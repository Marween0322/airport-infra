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
import datetime
 
# Create your views here.
from .models import Personal, Education, Eligibility, Experience, Voluntary, Learning

# PDS Sheet Pages
@login_required 
def Separate1(request):
    pds = Personal.objects.filter(author=request.user).first()
    education = Education.objects.filter(education_id=pds.id).order_by('date_from')
    educs = Education.objects.filter(education_id=pds.id).count()

    elig = Eligibility.objects.filter(eligible_id=pds.id).count()
    # Remove first 22 data for separate
    elig = int(elig) - 6
    # display last data after 18
    if elig >= 1:
        eligible = Eligibility.objects.filter(eligible_id=pds.id).order_by('-id')[:int(elig)]
    else:
        eligible = None
    

    exp = Experience.objects.filter(exp_id=pds.id).count()
    # Remove first 22 data for separate
    exp = int(exp) - 22
    # display last data after 18
    if exp >= 1:
        experience = Experience.objects.filter(exp_id=pds.id).order_by('exp_to')[:int(exp)]
    else:
        experience = None
    
    learn = Learning.objects.filter(learn_id=pds.id).exclude(Q(is_approve='For Review') | Q(is_approve='Disapproved')).count()
    # Remove first 18 data for separate
    learn = int(learn) - 18
    # display last data after 18
    if learn >= 1:
        learning = Learning.objects.filter(learn_id=pds.id).exclude(Q(is_approve='For Review') | Q(is_approve='Disapproved')).order_by('date_to')[:int(learn)]
    else:
        learning = None

    context = { 'pds' :pds, 'education': education, 'eligible': eligible, 'experience': experience,'learn' : learn, 'learning': learning}
    return render(request, 'pds/sheet/separate1.html', context)

@login_required 
def Separate2(request):
    pds = Personal.objects.filter(author=request.user).first()
    education = Education.objects.filter(education_id=pds.id).order_by('date_from')
    educs = Education.objects.filter(education_id=pds.id).count()

    elig = Eligibility.objects.filter(eligible_id=pds.id).count()
    # Remove first 22 data for separate
    elig = int(elig) - 6
    # display last data after 18
    if elig >= 1:
        eligible = Eligibility.objects.filter(eligible_id=pds.id).order_by('-id')[:int(elig)]
    else:
        eligible = None
    

    exp = Experience.objects.filter(exp_id=pds.id).count()
    # Remove first 22 data for separate
    exp = int(exp) - 22
    # display last data after 18
    if exp >= 1:
        experience = Experience.objects.filter(exp_id=pds.id).order_by('exp_to')[:int(exp)]
    else:
        experience = None
    
    learn = Learning.objects.filter(learn_id=pds.id).exclude(Q(is_approve='For Review') | Q(is_approve='Disapproved')).count()
    # Remove first 18 data for separate
    learn = int(learn) - 18
    # display last data after 18
    if learn >= 1:
        learning = Learning.objects.filter(learn_id=pds.id).exclude(Q(is_approve='For Review') | Q(is_approve='Disapproved')).order_by('date_to')[:int(learn)]
    else:
        learning = None

    context = { 'pds' :pds, 'education': education, 'eligible': eligible, 'experience': experience,'learn' : learn, 'learning': learning}
    return render(request, 'pds/sheet/separate1.html', context)
