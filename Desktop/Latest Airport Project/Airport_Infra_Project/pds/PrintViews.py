from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.template import loader
from django.urls import reverse
from django.template.loader import render_to_string, get_template 
from django.utils import timezone
from django.views import View

from django.views import generic 
import datetime
from io import BytesIO
# PDF Import HTML to PDF
from xhtml2pdf import pisa 
from django.db.models import Sum


# Create your views here.
from .models import Personal, Payroll, Children, Education, Eligibility, Experience, Voluntary, Learning, Otherinfo, Refferences, Other_skills, Other_recognitions, Other_membership, Vaccine, Training

# PDFViews
# @login_required
def render_to_pdf(template_src, context_dict={}): 
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1", 'ignore')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


#Opens up page as PDF
class ViewPDFPage1(View):
    def get(self, request, *args, **kwargs):
        # PDS Sheet Pages
        pds = Personal.objects.filter(author=request.user).first()
        today = datetime.date.today()
        children = Children.objects.filter(child_id=pds.id).order_by('-birth_date')
        childs = Children.objects.filter(child_id=pds.id).count()
        education = Education.objects.filter(education_id=pds.id).order_by('date_from')
        educs = Education.objects.filter(education_id=pds.id).count()

        data = {
            "pds": pds,
            "today": today,
            "children": children,
            "childs": childs,
            "education": education,
            "educs": educs,
            }

        pdf = render_to_pdf('pds/print/page1.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class ViewPDFPage2(View):
    def get(self, request, *args, **kwargs):
        # PDS Sheet Pages
        pds = Personal.objects.filter(author=request.user).first()
        today = datetime.date.today()
        
        eligible = Eligibility.objects.filter(eligible_id=pds.id)
        elig = Eligibility.objects.filter(eligible_id=pds.id).count()
        experience = Experience.objects.filter(exp_id=pds.id).order_by('-exp_to')
        exp = Experience.objects.filter(exp_id=pds.id).count()
        

        data = {
            "pds": pds,
            "today": today,
            "eligible": eligible,
            "elig": elig,
            "experience": experience,
            "exp": exp,
            }

        pdf = render_to_pdf('pds/print/page1.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class ViewPDFPage3(View):
    def get(self, request, *args, **kwargs):
        # PDS Sheet Pages
        pds = Personal.objects.filter(author=request.user).first()
        today = datetime.date.today()
        
        voluntary = Voluntary.objects.filter(voluntary_id=pds.id)
        volun = Voluntary.objects.filter(voluntary_id=pds.id).count()
        # learning = Learning.objects.filter(learn_id=pds.id).exclude(is_approve='For Review')
        # learn = Learning.objects.filter(learn_id=pds.id).exclude(is_approve='For Review').count()
        learning = Learning.objects.filter(learn_id=pds.id).order_by('-date_to')
        learn = Learning.objects.filter(learn_id=pds.id).count()
        other_skills = Other_skills.objects.filter(ski_id=pds.id)
        skills = Other_skills.objects.filter(ski_id=pds.id).count()
        other_recognitions = Other_recognitions.objects.filter(recog_id=pds.id)
        recognitions = Other_recognitions.objects.filter(recog_id=pds.id).count()
        other_membership = Other_membership.objects.filter(member_id=pds.id)
        membership = Other_membership.objects.filter(member_id=pds.id).count()

        data = {
            "pds": pds,
            "today": today,
            "voluntary": voluntary,
            "volun": volun,
            "learning": learning,
            "learn": learn,
            "other_skills": other_skills,
            "skills": skills,
            "other_recognitions": other_recognitions,
            "recognitions": recognitions,
            "other_membership": other_membership,
            "membership": membership,    
            }

        pdf = render_to_pdf('pds/print/page1.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class ViewPDFPage4(View):
    def get(self, request, *args, **kwargs):
        # PDS Sheet Pages
        pds = Personal.objects.filter(author=request.user).first()
        today = datetime.date.today()
        
        otherinfo = Otherinfo.objects.filter(otherinfo_id=pds.id).first()
        refers = Refferences.objects.filter(refer_id=pds.id)[:3]
        refer_count = Refferences.objects.filter(refer_id=pds.id).count()

        data = {
            "pds": pds,
            "today": today, 
            "otherinfo": otherinfo,
            "refers": refers,
            "refer_count": refer_count,
            }

        pdf = render_to_pdf('pds/print/page1.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
