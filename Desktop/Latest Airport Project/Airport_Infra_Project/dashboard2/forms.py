from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import filesizeformat
from django.conf import settings

from .models import Bulletin, BulletinFile, Aknowledge, BulletinComment, AiportProject, AiportProfile
    

class BulletinForm(forms.ModelForm):

      class Meta:
            model = Bulletin
            fields = "__all__"  

class BulletinCommentForm(forms.ModelForm):

      class Meta:
            model = BulletinComment
            fields = "__all__"  

class AiportProjectForm(forms.ModelForm):

      class Meta:
            model = AiportProject
            fields = "__all__"  

class AiportProfileForm(forms.ModelForm):

      class Meta:
            model = AiportProfile
            fields = "__all__"  
