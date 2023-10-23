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
import datetime
 
# Create your views here.
from .models import Personal,Payroll, Children, Education, Eligibility, Experience, Voluntary, Learning, Otherinfo, Refferences, Other_skills, Other_recognitions, Other_membership, Position, Post
from .forms import PersonalInfoForm, ChildrenForm, EducationForm, EligibilityForm, ExperienceForm, VoluntaryForm, LearningForm, OtherinfoForm, RefferencesForm, Other_membershipForm, Other_recognitionsForm, Other_skillsForm

# Sign Up View
class  SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False # Deactivate account till it is confirmed
            user.save()
            print(form)
            print("Invalid Form")
            print(form.errors)
            messages.success(request, 'Account has been Created, You may login... ' + str(user.username))
            return HttpResponseRedirect('/pds')
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            return render(request,'registration/sign_up.html',{'form':form})
            # return redirect('/pds/signup')

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

# Home Page
@login_required
def index(request):
    pds = Personal.objects.filter(author=request.user.id).first()
    payroll = Payroll.objects.filter(payroll=request.user.id).first()
    data1 = Post.objects.filter(status='Active').filter(post_type='Reorg').last()
    data2 = Post.objects.filter(status='Active').filter(post_type='Announcement').last()
    data3 = Post.objects.filter(status='Active').filter(post_type='QnA').last()
    datetoday = datetime.datetime.now()
    today = datetoday.strftime('%B %d, %Y')
    data = Post.objects.filter(status='Active').filter(post_type='Announcement').order_by('-post_date')[:10]

    if request.user.groups.filter(name='odg').exists():
        group_odg = "yes"
    else:
        group_odg = "no"

    if request.user.groups.filter(name='memo').exists():
        group_memo = "yes"
    else:
        group_memo = "no"

    context = {'data':data ,'pds': pds,'data1': data1,'data2': data2,'data3': data3, 'payroll':payroll, 'today': today, 'group_odg': group_odg , 'group_memo': group_memo}
    return render(request, 'pds/personalinfo/index.html', context)

# home View after user create
@login_required 
def home(request):
    return render(request, 'pds/home.html')

@login_required 
def PersonalDetail(request, personal_id):
    try:
        personal = Personal.objects.get(pk=personal_id)
    except Personal.DoesNotExist:
        raise get_object_or_404("PDS does not exist")
    return render(request, 'pds/personalinfo/detail.html', {'personal': personal})

# Display Personal Information Page
@login_required
def PersonalPDS1(request):
    pds = Personal.objects.filter(author=request.user).first()
    if  pds:
        children = Children.objects.filter(child_id=pds.id).order_by('-birth_date')
        education = Education.objects.filter(education_id=pds.id).order_by('-date_from')
        eligibility = Eligibility.objects.filter(eligible_id=pds.id).order_by('-exam_date')
        experience = Experience.objects.filter(exp_id=pds.id).order_by('-exp_from')
        voluntary = Voluntary.objects.filter(voluntary_id=pds.id).order_by('-vol_from')
        learning = Learning.objects.filter(learn_id=pds.id).order_by('-date_from')
        otherinfo = Otherinfo.objects.filter(otherinfo_id=pds.id).first()
        refferences = Refferences.objects.filter(refer_id=pds.id)
        other_skills = Other_skills.objects.filter(ski_id=pds.id)
        other_recognitions = Other_recognitions.objects.filter(recog_id=pds.id)
        other_membership = Other_membership.objects.filter(member_id=pds.id)
        context = {'pds': pds, 'children': children, 'education': education , 'other_recognitions': other_recognitions , 'other_membership': other_membership , 'eligibility': eligibility , 'experience': experience , 'voluntary': voluntary , 'learning': learning , 'otherinfo': otherinfo , 'refferences': refferences , 'other_skills': other_skills }
        if pds.status == "For Approval":
            return redirect('/pds')
        return render(request, 'pds/personal/index.html', context)
    else:
        return redirect('/pds')

# Display Personal Information Page
@login_required
def PersonalPDS(request):
    pds = Personal.objects.filter(author=request.user).first()
    if  pds:
        children = Children.objects.filter(child_id=pds.id).order_by('-birth_date')    
        childs = Children.objects.filter(child_id=pds.id).count()
        education = Education.objects.filter(education_id=pds.id).order_by('-date_from')    
        educs = Education.objects.filter(education_id=pds.id).count()
        today = datetime.date.today()
        context = {'pds': pds, 'children': children, 'childs' : childs,'educs' : educs, 'education': education ,'today': today}
        if pds.status == "For Approval":
            return redirect('/pds')
        return render(request, 'pds/personal/page1.html', context) 
    else:
        return redirect('/pds')

# Display Personal Information Page
@login_required
def PersonalPDS2(request):
    pds = Personal.objects.filter(author=request.user).first()
    if pds:
            eligible = Eligibility.objects.filter(eligible_id=pds.id)
            elig = Eligibility.objects.filter(eligible_id=pds.id).count()
            experience = Experience.objects.filter(exp_id=pds.id).order_by('-exp_to')
            exp = Experience.objects.filter(exp_id=pds.id).count()
            today = datetime.date.today()
            context = {'eligible': eligible, 'elig': elig, 'experience': experience, 'exp': exp,'today': today}
            if pds.status == "For Approval":
                return redirect('/pds')
            return render(request, 'pds/personal/page2.html', context) 
    else:
        return redirect('/pds')

# Display Personal Information Page
@login_required
def PersonalPDS3(request):
    pds = Personal.objects.filter(author=request.user).first()
    if pds:
            voluntary = Voluntary.objects.filter(voluntary_id=pds.id)
            volun = Voluntary.objects.filter(voluntary_id=pds.id).count()
            learning = Learning.objects.filter(learn_id=pds.id).order_by('-date_to')
            learn = Learning.objects.filter(learn_id=pds.id).count()
            other_skills = Other_skills.objects.filter(ski_id=pds.id)
            skills = Other_skills.objects.filter(ski_id=pds.id).count()
            other_recognitions = Other_recognitions.objects.filter(recog_id=pds.id)
            recognitions = Other_recognitions.objects.filter(recog_id=pds.id).count()
            other_membership = Other_membership.objects.filter(member_id=pds.id)
            membership = Other_membership.objects.filter(member_id=pds.id).count()
            today = datetime.date.today()
            context = {'voluntary': voluntary, 'volun': volun, 'learning': learning, 'learn': learn, 'other_skills': other_skills, 'skills': skills, 'other_recognitions': other_recognitions, 'recognitions': recognitions, 'other_membership': other_membership, 'membership': membership,'today': today}
            if pds.status == "For Approval":
                return redirect('/pds')
            return render(request, 'pds/personal/page3.html', context)
    else:
        return redirect('/pds')

# Display Personal Information Page
@login_required
def PersonalPDS4(request):
    pds = Personal.objects.filter(author=request.user).first()
    if pds:
            otherinfo = Otherinfo.objects.filter(otherinfo_id=pds.id).first()
            refers = Refferences.objects.filter(refer_id=pds.id)[:3]
            refer_count = Refferences.objects.filter(refer_id=pds.id).count()

            context = {'pds' : pds ,'otherinfo': otherinfo,'refers': refers,'refer_count': refer_count}
            if pds.status == "For Approval":
                return redirect('/pds')
            return render(request, 'pds/personal/page4.html', context) 
    else:
        return redirect('/pds')

@login_required 
def InfoCreate(request):
    if request.method == "POST":
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            try:
                pds = Personal.objects.filter(author=request.user).first()
                if pds:
                    messages.success(request, 'PDS already exsisted.')
                    return redirect('/pds')
                else:
                    position = Position.objects.get(position_id=request.POST['position_title'])
                    form.save()
                    instance = form.save(commit=False)
                    instance.author = request.user
                    instance.position_title = position.name
                    instance.tech_none = position.classification
                    instance.gcg_sdd = position.gcg
                    instance.dotr_level = position.dotr
                    instance.position_id = position.position_id
                    if request.POST['same_address'] == "Yes":
                        if request.POST['res_numstreet'] != '':
                            instance.perma_numstreet = request.POST['res_numstreet']
                        if request.POST['res_region'] != '':
                            instance.perma_region = request.POST['res_region']
                        if request.POST['res_brgy'] != '':
                            instance.perma_brgy = request.POST['res_brgy']
                        if request.POST['res_city'] != '':
                            instance.perma_city = request.POST['res_city']
                        if request.POST['res_province'] != '':
                            instance.perma_province = request.POST['res_province']
                        if request.POST['res_zip'] != '':
                            instance.perma_zip = request.POST['res_zip']
                    instance.save()
                    account = User.objects.get(id=request.user.id)
                    account.id = request.user.id
                    account.first_name = request.POST['first_name']
                    account.last_name = request.POST['surname']
                    account.email = request.POST['email']
                    account.save()
                    return redirect('/pds/personalinfo')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/personalinfo/create.html',{'form':form})
    form = PersonalInfoForm(request.POST)
    return render(request,'pds/personalinfo/create.html',{'form':form})

@login_required 
def InfoEdit(request, id):
    pds = Personal.objects.get(id=id)
    if(pds.author == request.user):
        return render(request,'pds/personalinfo/edit.html', {'pds':pds})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required 
def InfoUpdate(request, id):
    pds = Personal.objects.get(id=id)
    if (pds.author == request.user):    
        if request.POST:
            pds = Personal.objects.get(id=id)
            form = PersonalInfoForm(request.POST, instance=pds)
            if form.is_valid():            
                position = Position.objects.get(position_id=request.POST['position_title'])
                pds = Personal.objects.get(id=id)
                instance = form.save(commit=False)
                instance.personal_id = pds.id
                instance.position_title = position.name
                instance.tech_none = position.classification
                instance.gcg_sdd = position.gcg
                instance.position_id = position.position_id
                instance.dotr_level = position.dotr
                instance.item = pds.item
                instance.actual_annual = pds.actual_annual
                instance.salary_grade = pds.salary_grade
                instance.salary_id = pds.salary_id
                instance.job_level = pds.job_level
                instance.step = pds.step
                instance.rate = pds.rate
                instance.last_promotion = pds.last_promotion
                instance.original_appointment = pds.original_appointment
                instance.mode_separate = pds.mode_separate 
                instance.separate_date = pds.separate_date
                instance.edited_by = pds.edited_by
                instance.author = request.user
                if request.POST['same_address'] == "Yes":
                            if request.POST['res_numstreet'] != '':
                                instance.perma_numstreet = request.POST['res_numstreet']
                            if request.POST['res_region'] != '':
                                instance.perma_region = request.POST['res_region']
                            if request.POST['res_brgy'] != '':
                                instance.perma_brgy = request.POST['res_brgy']
                            if request.POST['res_city'] != '':
                                instance.perma_city = request.POST['res_city']
                            if request.POST['res_province'] != '':
                                instance.perma_province = request.POST['res_province']
                            if request.POST['res_zip'] != '':
                                instance.perma_zip = request.POST['res_zip']
                instance.save()
                return redirect('/pds/personalinfo')
            return render(request,'pds/personalinfo/edit.html', {'form':form, 'pds': pds})
        return redirect('/pds/personalinfo')

# Upload Photo
@login_required
def PhotoUpload(request, id):
    pds = Personal.objects.get(id=id)
   
    if (pds.author == request.user):
        return render(request,'pds/photo/upload.html', {'pds':pds})
    else:
        return HttpResponseRedirect(reverse('pds:index'))

@login_required 
def PhotoUpdate(request, id):
    pds = Personal.objects.get(id=id)
    if (pds.author == request.user):
        if request.method == 'POST':
            pds = Personal.objects.get(id=id)
            form = PersonalInfoForm(request.POST, request.FILES, instance = pds)
            # return HttpResponse(request.FILES)
            if form.is_valid():
                pds = Personal.objects.get(id=id)
                pds.photo = request.FILES['photo']
                pds.save()
                return redirect('/pds/personalinfo4')
            context = {'pds':pds,'form':form }
            return render(request,'pds/status/edit.html', context)
        return redirect('/pds/personalinfo4')
    return redirect('/pds/personalinfo4')

# Children Views
@login_required 
def ChildrenlCreate(request):
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = ChildrenForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                instance = form.save(commit=False)
                instance.child_id = info.id
                instance.save()
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return redirect('/pds/personalinfo')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/children/create.html',{'form':form})
    form = ChildrenForm(request.POST)
    return render(request,'pds/children/create.html',{'form':form})

@login_required 
def ChildEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    chi = Children.objects.get(id=id)
    if(chi.child.id == info.id):
        return render(request,'pds/children/edit.html', {'chi':chi})
    else:
        return redirect('/pds/personalinfo')

@login_required 
def ChildUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        chi = Children.objects.get(id=id)
        form = ChildrenForm(request.POST, instance=chi)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.child_id = info.id
            instance.save()
            return redirect('/pds/personalinfo')
        return render(request,'pds/personalinfo/edit.html', {'form':form})
    return redirect('/pds/personalinfo')

# Education Views
@login_required 
def EducationCreate(request):
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = EducationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                instance = form.save(commit=False)
                instance.education_id = info.id
                instance.save()
                return redirect('/pds/personalinfo')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/education/create.html',{'form':form})
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            messages.success(request, 'Submit error!.')
            return render(request,'pds/education/create.html',{'form':form})
    form = EducationForm(request.POST)
    return render(request,'pds/education/create.html',{'form':form})

@login_required 
def EducationEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    educ = Education.objects.get(id=id)
    if(educ.education.id == info.id):
        return render(request,'pds/education/edit.html', {'educ':educ})
    else:
        return redirect('/pds/personalinfo')

@login_required 
def EducationUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        educ = Education.objects.get(id=id)
        form = EducationForm(request.POST, instance=educ)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.education_id = info.id
            instance.save()
            return redirect('/pds/personalinfo')
        return render(request,'pds/education/edit.html', {'form':form})
    return redirect('/pds/personalinfo')


 # eligibility Views
@login_required 
def EligibilityCreate(request):
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = EligibilityForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                instance = form.save(commit=False)
                instance.eligible_id = info.id
                instance.save()
                return redirect('/pds/personalinfo2')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/eligibility/create.html',{'form':form})
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            messages.success(request, 'Submit error!.')
            return render(request,'pds/eligibility/create.html',{'form':form})
    form = EligibilityForm(request.POST)
    return render(request,'pds/eligibility/create.html',{'form':form})

@login_required 
def EligibilityEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    eligible = Eligibility.objects.get(id=id)
    if(eligible.eligible.id == info.id):
        return render(request,'pds/eligibility/edit.html', {'eligible':eligible})
    else:
        return redirect('/pds/personalinfo')

@login_required 
def EligibilityUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        eligible = Eligibility.objects.get(id=id)
        form = EligibilityForm(request.POST, instance=eligible)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.eligible_id = info.id
            instance.save()
            return redirect('/pds/personalinfo2')
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            messages.success(request, 'Submit error!.')
            return render(request,'pds/eligibility/edit.html', {'form':form})
    return redirect('/pds/personalinfo')

# Experience Views
@login_required 
def ExperienceCreate(request):
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = ExperienceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                instance = form.save(commit=False)
                instance.exp_id = info.id
                instance.save()
                messages.success(request, 'Experience  '  + str(instance.position) + ' Added.')
                return redirect('/pds/personalinfo2')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/experience/create.html',{'form':form})
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            messages.success(request, 'Submit error!.') 
            return render(request,'pds/experience/create.html',{'form':form}) 
    form = ExperienceForm(request.POST)
    return render(request,'pds/experience/create.html',{'form':form})

@login_required 
def ExperienceEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    exp = Experience.objects.get(id=id)
    if(exp.exp.id == info.id):
        return render(request,'pds/experience/edit.html', {'exp':exp})
    else:
        return redirect('/pds/personalinfo2')

@login_required 
def ExperienceUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        exp = Experience.objects.get(id=id)
        form = ExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.exp_id = info.id
            instance.save()
            return redirect('/pds/personalinfo2')
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            messages.success(request, 'Submit error!.')  
            return render(request,'pds/experience/edit.html', {'form':form})
    return redirect('/pds/personalinfo2')

# Voluntary Views
@login_required 
def VoluntaryCreate(request):
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = VoluntaryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                instance = form.save(commit=False)
                instance.voluntary_id = info.id
                instance.save()
                return redirect('/pds/personalinfo3')

            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/voluntary/create.html',{'form':form})
    form = VoluntaryForm(request.POST)
    return render(request,'pds/voluntary/create.html',{'form':form})

@login_required 
def VoluntaryEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    vol = Voluntary.objects.get(id=id)
    if(vol.voluntary.id == info.id):
        return render(request,'pds/voluntary/edit.html', {'vol':vol})
    else:
        return redirect('/pds/personalinfo3')

@login_required 
def VoluntaryUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        vol = Voluntary.objects.get(id=id)
        form = VoluntaryForm(request.POST, instance=vol)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.voluntary_id = info.id
            instance.save()
            return redirect('/pds/personalinfo3')
        return render(request,'pds/voluntary/edit.html', {'form':form})
    return redirect('/pds/personalinfo3')

# Learning Views
@login_required 
def LearningCreate(request): 
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = LearningForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                instance = form.save(commit=False)
                instance.learn_id = info.id
                instance.save()
                return redirect('/pds/personalinfo3')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                messages.success(request, 'Submit error!.')
                return render(request,'pds/learning/create.html',{'form':form})
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            messages.success(request, 'Submit error!.')
            return render(request,'pds/learning/create.html',{'form':form})
    form = LearningForm(request.POST)
    return render(request,'pds/learning/create.html',{'form':form})

@login_required 
def LearningEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    learn = Learning.objects.get(id=id)
    if(learn.learn.id == info.id):
        return render(request,'pds/learning/edit.html', {'learn':learn})
    else:
        return redirect('/pds/personalinfo3')

@login_required 
def LearningUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        learn = Learning.objects.get(id=id)
        form = LearningForm(request.POST,request.FILES, instance=learn)
        if request.FILES.get('file'):
            file_check = 'True'
        else:
            file_check = 'False'
        if form.is_valid():
                        
            instance = form.save(commit=False)
            instance.learn_id = info.id
            if file_check == 'True' :
                    instance.file = request.FILES['file']
            else:
                    instance.file = learn.file
            instance.date_to = request.POST['date_to']
            instance.date_from = request.POST['date_from']
            instance.training_hours = request.POST['training_hours']
            instance.save()
            return redirect('/pds/personalinfo3')
        return render(request,'pds/learning/edit.html', {'form':form})
    return redirect('/pds/personalinfo3')

# Otherinfo Views
@login_required 
def OtherinfoCreate(request):
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = OtherinfoForm(request.POST,request.FILES)
        if form.is_valid():
                form.save()
                instance = form.save(commit=False)
                instance.otherinfo_id = info.id
                instance.save()
                return redirect('/pds/personalinfo4')
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            messages.success(request, 'Submit error!.')            
            return render(request,'pds/otherinfo/create.html',{'form':form})
    form = OtherinfoForm(request.POST)
    return render(request,'pds/otherinfo/create.html',{'form':form})

@login_required 
def OtherinfoEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    other = Otherinfo.objects.get(id=id)
    if(other.otherinfo.id == info.id):
        return render(request,'pds/otherinfo/edit.html', {'other':other})
    else:
        return redirect('/pds/personalinfo')

@login_required 
def OtherinfoUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        other = Otherinfo.objects.get(id=id)
        form = OtherinfoForm(request.POST,request.FILES, instance=other)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.otherinfo_id = info.id
            instance.save()
            return redirect('/pds/personalinfo4')
        return render(request,'pds/otherinfo/edit.html', {'form':form})
    return redirect('/pds/personalinfo')

# Skills Views
@login_required 
def SkillsCreate(request):
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = Other_skillsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                instance = form.save(commit=False)
                instance.ski_id = info.id
                instance.save()
                return redirect('/pds/personalinfo3')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/skills/create.html',{'form':form})
    form = Other_skillsForm(request.POST)
    return render(request,'pds/skills/create.html',{'form':form})

@login_required 
def SkillsEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    ski = Other_skills.objects.get(id=id)
    if(ski.ski.id == info.id):
        return render(request,'pds/skills/edit.html', {'ski':ski})
    else:
        return redirect('/pds/personalinfo3')

@login_required 
def SkillsUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        ski = Other_skills.objects.get(id=id)
        form = Other_skillsForm(request.POST, instance=ski)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.ski_id = info.id
            instance.save()
            return redirect('/pds/personalinfo3')
        return render(request,'pds/skills/edit.html', {'form':form})
    return redirect('/pds/personalinfo3')

# Recognitions Views
@login_required 
def RecognitionsCreate(request):
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = Other_recognitionsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                instance = form.save(commit=False)
                instance.recog_id = info.id
                instance.save()
                return redirect('/pds/personalinfo3')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/recognition/create.html',{'form':form})
    form = Other_recognitionsForm(request.POST)
    return render(request,'pds/recognition/create.html',{'form':form})

@login_required 
def RecognitionsEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    recog = Other_recognitions.objects.get(id=id)
    if(recog.recog.id == info.id):
        return render(request,'pds/recognition/edit.html', {'recog':recog})
    else:
        return redirect('/pds/personalinfo3')

@login_required 
def RecognitionsUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        recog = Other_recognitions.objects.get(id=id)
        form = Other_recognitionsForm(request.POST, instance=recog)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.recog_id = info.id
            instance.save()
            return redirect('/pds/personalinfo3')
        return render(request,'pds/recognition/edit.html', {'form':form})
    return redirect('/pds/personalinfo3')

# Membership Views
@login_required 
def MembershipCreate(request):
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = Other_membershipForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                instance = form.save(commit=False)
                instance.member_id = info.id
                instance.save()
                return redirect('/pds/personalinfo3')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/membership/create.html',{'form':form})
    form = Other_membershipForm(request.POST)
    return render(request,'pds/membership/create.html',{'form':form})

@login_required 
def MembershipEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    member = Other_membership.objects.get(id=id)
    if(member.member.id == info.id):
        return render(request,'pds/membership/edit.html', {'member':member})
    else:
        return redirect('/pds/personalinfo3')

@login_required 
def MembershipUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        member = Other_membership.objects.get(id=id)
        form = Other_membershipForm(request.POST, instance=member)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.member_id = info.id
            instance.save()
            return redirect('/pds/personalinfo3')
        return render(request,'pds/membership/edit.html', {'form':form})
    return redirect('/pds/personalinfo3')

# Refferences Views
@login_required 
def RefferencesCreate(request):
    
    if request.method == "POST":
        info = Personal.objects.filter(author=request.user).first()
        form = RefferencesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                instance = form.save(commit=False)
                instance.refer_id = info.id
                instance.save()
                return redirect('/pds/personalinfo4')
            except: 
                print(form)
                print("Invalid Form")
                print(form.errors)
                return render(request,'pds/refference/create.html',{'form':form})
    form = RefferencesForm(request.POST)
    return render(request,'pds/refference/create.html',{'form':form})

@login_required 
def RefferencesEdit(request, id):
    info = Personal.objects.filter(author=request.user).first()
    refer = Refferences.objects.get(id=id)
    if(refer.refer.id == info.id):
        return render(request,'pds/refference/edit.html', {'refer':refer})
    else:
        return redirect('/pds/personalinfo4')

@login_required 
def RefferencesUpdate(request, id):
    if request.POST:
        info = Personal.objects.filter(author=request.user).first()
        refer = Refferences.objects.get(id=id)
        form = RefferencesForm(request.POST, instance=refer)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.refer_id = info.id
            instance.save()
            return redirect('/pds/personalinfo4')
        return render(request,'pds/refference/edit.html', {'form':form})
    return redirect('/pds/personalinfo4')


# PDS Sheet Pages
@login_required 
def Page1(request):
    pds = Personal.objects.filter(author=request.user).first()
    children = Children.objects.filter(child_id=pds.id).order_by('-birth_date')
    childs = Children.objects.filter(child_id=pds.id).count()
    education = Education.objects.filter(education_id=pds.id).order_by('date_from')
    educs = Education.objects.filter(education_id=pds.id).count()
    today = datetime.date.today()
    context = {'pds': pds, 'children': children, 'childs' : childs,'educs' : educs, 'education': education ,'today': today}
    return render(request, 'pds/sheet/page1.html', context)

@login_required 
def Page2(request):
    pds = Personal.objects.filter(author=request.user).first()
    eligible = Eligibility.objects.filter(eligible_id=pds.id)[:6]
    elig = Eligibility.objects.filter(eligible_id=pds.id).count()
    experience = Experience.objects.filter(exp_id=pds.id).order_by('-exp_to')[:22]
    exp = Experience.objects.filter(exp_id=pds.id).count()
    today = datetime.date.today()
    context = {'eligible': eligible, 'elig': elig, 'experience': experience, 'exp': exp,'today': today}
    return render(request, 'pds/sheet/page2.html', context)

@login_required 
def Page3(request):
    pds = Personal.objects.filter(author=request.user).first()
    voluntary = Voluntary.objects.filter(voluntary_id=pds.id)
    volun = Voluntary.objects.filter(voluntary_id=pds.id).count()
    learning = Learning.objects.filter(learn_id=pds.id).exclude(Q(is_approve='For Review') | Q(is_approve='Disapproved')).order_by('-date_to')[:20]
    learn = Learning.objects.filter(learn_id=pds.id).exclude(Q(is_approve='For Review') | Q(is_approve='Disapproved')).count()
    # learning = Learning.objects.filter(learn_id=pds.id).order_by('-date_to')
    # learn = Learning.objects.filter(learn_id=pds.id).count()

    other_skills = Other_skills.objects.filter(ski_id=pds.id)
    skills = Other_skills.objects.filter(ski_id=pds.id).count()
    other_recognitions = Other_recognitions.objects.filter(recog_id=pds.id)
    recognitions = Other_recognitions.objects.filter(recog_id=pds.id).count()
    other_membership = Other_membership.objects.filter(member_id=pds.id)
    membership = Other_membership.objects.filter(member_id=pds.id).count()
    today = datetime.date.today()
    context = {'voluntary': voluntary, 'volun': volun, 'learning': learning, 'learn': learn, 'other_skills': other_skills, 'skills': skills, 'other_recognitions': other_recognitions, 'recognitions': recognitions, 'other_membership': other_membership, 'membership': membership,'today': today}
    return render(request, 'pds/sheet/page3.html', context)

@login_required 
def Page4(request):
    pds = Personal.objects.filter(author=request.user).first()
    otherinfo = Otherinfo.objects.filter(otherinfo_id=pds.id).first()
    refers = Refferences.objects.filter(refer_id=pds.id)[:3]
    refer_count = Refferences.objects.filter(refer_id=pds.id).count()
    today = datetime.date.today()

    context = {'otherinfo': otherinfo,'refers': refers,'refer_count': refer_count,'today': today}
    return render(request, 'pds/sheet/page4.html', context) 



