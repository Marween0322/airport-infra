from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib import admin
from decimal import * 
from datetime import datetime

# Qr Code
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here. 

class Personal(models.Model): 
    author = models.OneToOneField(User, db_column="user_id", related_name='pds_info', on_delete=models.CASCADE,null=True, blank=True, unique=True)
    assignment = models.CharField(max_length=200,null=True, blank=True)
    emp_type = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=200,null=True, blank=True) 
    service = models.CharField(max_length=200,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    middle_name = models.CharField(max_length=200,null=True, blank=True)
    ext_name = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.DateField('birth',null=True, blank=True)
    birth_place = models.CharField(max_length=200,null=True, blank=True, verbose_name='Place of Birth')
    sex = models.CharField(max_length=200,null=True, blank=True)
    civil_status = models.CharField(max_length=200,null=True, blank=True, verbose_name='Civil Status')
    height = models.CharField(max_length=20,null=True, blank=True)
    weight = models.CharField(max_length=20,null=True, blank=True)
    blood_type = models.CharField(max_length=200,null=True, blank=True, verbose_name='Blood Type')
    gsis = models.CharField(max_length=200,null=True, blank=True, verbose_name='GSIS')
    pagibig = models.CharField(max_length=200,null=True, blank=True, verbose_name='Pag-Ibig')
    philhealth = models.CharField(max_length=2002,null=True, blank=True, verbose_name='SSS')
    sss = models.CharField(max_length=200,null=True, blank=True, verbose_name='TIN')
    tin = models.CharField(max_length=200,null=True, blank=True)
    emp_number = models.CharField(max_length=200,null=True, blank=True, verbose_name='Employee Number')
    citizenship = models.CharField(max_length=200,null=True, blank=True)
    citizen_detail = models.CharField(max_length=200, blank=True, null=True, verbose_name='Citizenship Detail')
    citizen_country = models.CharField(max_length=200, blank=True, null=True, verbose_name='Citizenship Country')
    res_numstreet = models.CharField(max_length=200,null=True, blank=True, verbose_name='Residence Street Name')
    res_region = models.CharField(max_length=200,null=True, blank=True, verbose_name='Residence Region')
    res_brgy = models.CharField(max_length=200,null=True, blank=True, verbose_name='Residence Barangay')
    res_city = models.CharField(max_length=200,null=True, blank=True, verbose_name='Residence City')
    res_province = models.CharField(max_length=200,null=True, blank=True, verbose_name='Residence Province')
    res_zip = models.CharField(max_length=10,null=True, blank=True, verbose_name='Residence ZIP CODE')
    perma_numstreet = models.CharField(max_length=200,null=True, blank=True, verbose_name='Permanet Street Name')
    perma_brgy = models.CharField(max_length=200,null=True, blank=True, verbose_name='Permanet Barangay')
    perma_city = models.CharField(max_length=200,null=True, blank=True, verbose_name='Permanet perma_city')
    perma_province = models.CharField(max_length=200,null=True, blank=True, verbose_name='Permanet Province')
    perma_zip = models.CharField(max_length=10,null=True, blank=True, verbose_name='Permanet ZIP CODE')
    telephone = models.CharField(max_length=20,null=True, blank=True)
    mobile = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    spouse_surname = models.CharField(max_length=200, blank=True, null=True, verbose_name='Spouse Surname')
    spouse_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Spouse First Name')
    spouse_middle = models.CharField(max_length=200, blank=True, null=True, verbose_name='Spouse Middle Name')
    spouse_ext = models.CharField(max_length=200, blank=True, null=True , verbose_name='Spouse Extension Name')
    spouse_occupation = models.CharField(max_length=200, blank=True, null=True , verbose_name='Spouse Occupation')
    emb_biz = models.CharField(max_length=200, blank=True, null=True, verbose_name='Emploer Name')
    emb_biz_add = models.CharField(max_length=200, blank=True, null=True, verbose_name='Employer Address')
    phone = models.CharField(max_length=20,null=True, blank=True)
    dad_surname = models.CharField(max_length=200, blank=True, null=True, verbose_name='Father Surname')
    dad_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Father Middle Name')
    dad_middle = models.CharField(max_length=200, blank=True, null=True, verbose_name='Father First Name')
    dad_ext = models.CharField(max_length=200, blank=True, null=True, verbose_name='Father Middle Name')
    mom_surname = models.CharField(max_length=200, blank=True, null=True, verbose_name='Mother Surname')
    mom_name = models.CharField(max_length=200, blank=True, null=True , verbose_name='Mother First Name')
    mom_middle = models.CharField(max_length=200, blank=True, null=True, verbose_name='Mother Middle Name')
    # Additional Fields
    salary_grade = models.CharField(max_length=200, blank=True, null=True, verbose_name='Salary Grade')
    salary_id = models.CharField(max_length=200, blank=True, null=True)
    job_level = models.CharField(max_length=200, blank=True, null=True, verbose_name='Job Level')
    step = models.CharField(max_length=200, blank=True, null=True, verbose_name='Step Increment')
    rate = models.CharField(max_length=200, blank=True, null=True, verbose_name='Monthly Rate')
    last_promotion = models.DateField('last_promotion',null=True, blank=True)
    original_appointment = models.DateField('original_appointment',null=True, blank=True)
    photo = models.ImageField(upload_to= "photo/", default="photo/user-picture.png", blank=True)
    item = models.CharField(max_length=200,null=True, blank=True)
    mode_separate = models.CharField(max_length=200, blank=True, null=True, verbose_name='Mode of Separation')
    separate_date = models.DateField('separate_date',null=True, blank=True)
    position_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Position Tittle')
    status = models.CharField(max_length=200, blank=True, null=True, default='For Approval')
    org_unit = models.CharField(max_length=200, blank=True, null=True)
    auth_annual = models.CharField(max_length=200, blank=True, null=True)
    actual_annual = models.CharField(max_length=200, blank=True, null=True)
    rate_perday = models.CharField(max_length=200, blank=True, null=True)
    area_type = models.CharField(max_length=200, blank=True, null=True)
    tech_none = models.CharField(max_length=200, blank=True, null=True)
    dotr_level = models.CharField(max_length=200, blank=True, null=True)
    gcg_sdd = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    umid = models.CharField(max_length=200, blank=True, null=True)
    edited_by = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    contact_person_number = models.CharField(max_length=200, blank=True, null=True)
    contact_relation = models.CharField(max_length=200, blank=True, null=True)
    position_id = models.CharField(max_length=200, blank=True, null=True)


    @property
    def yos(self):
        if self.original_appointment is None:
            return(self.original_appointment)
        return int((datetime.now().date() - self.original_appointment).days / 365.25)

    @property
    def age(self):
        if self.birth_date is None:
            return(self.birth_date)
        return int((datetime.now().date() - self.birth_date).days / 365.25)
    @property
    def qr_img(self):
        return (Qrcode.objects.filter(qr_id= self.id).order_by('id').last())

    @property
    def UserName(self):
        return (User.objects.filter(username= self.author).last())

    @property
    def leaveC(self):
        return (Leave.objects.filter(leave_id= self.id).order_by('id').last())

    @property
    def pEligble(self):
        return (Eligibility.objects.filter(eligible_id= self.id).last())

    @property
    def pTrn(self):
        return (Learning.objects.filter(learn_id= self.id).order_by('date_to').last())

    @property
    def pEduc(self):
        return (Education.objects.filter(education_id= self.id).order_by('grad_year').last())

    
    def __str__(self):
        return f"{self.surname}, {self.first_name} {self.middle_name} - ({self.author})"

    def get_title_case_name(self):
        return self.surname.title(), self.first_name.title(), self.middle_name.title(), self.spouse_surname.title(), self.spouse_name.title(), self.spouse_middle.title(), self.dad_surname.title(), self.dad_name.title(), self.dad_middle.title(),  self.mom_surname.title(), self.mom_name.title(), self.mom_middle.title()

class Children(models.Model):
    child = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_child', on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200 ,null=True, blank=True)
    birth_date = models.DateField('birth',null=True, blank=True)

    # ...
    def __str__(self):
        return self.name

    def get_title_case_name(self):
        return self.name.title()

class Education(models.Model): 
    education = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_education', on_delete=models.CASCADE,null=True, blank=True)
    level = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    course  = models.CharField(max_length=200, blank=True, null=True)
    date_from = models.CharField(max_length=200, blank=True, null=True)
    date_to = models.CharField(max_length=200, blank=True, null=True)
    units  = models.CharField(max_length=200, blank=True, null=True)
    grad_year = models.CharField(max_length=10,blank=True, null=True)
    honors  = models.CharField(max_length=200, blank=True, null=True)

    # ...
    def __str__(self):
        return self.level

class Eligibility(models.Model):
    eligible = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_eligible', on_delete=models.CASCADE,null=True, blank=True)
    eligibility = models.CharField(max_length=200)
    rating  = models.CharField(max_length=200, null=True, blank=True)
    exam_date = models.DateField('date')
    place = models.CharField(max_length=200, blank=True, null=True)
    lic_number = models.CharField(max_length=10, null=True, blank=True)
    validity = models.DateField('validity',null=True, blank=True)

    # ...
    def __str__(self):
        return self.eligibility

class Experience(models.Model):
    exp = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_exp', on_delete=models.CASCADE,null=True, blank=True)
    exp_from = models.DateField('from',null=True, blank=True)
    exp_to = models.DateField('to',null=True, blank=True)
    position = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    salary = models.CharField(max_length=10,null=True, blank=True)
    increment = models.CharField(max_length=200,null=True, blank=True)
    appointment = models.CharField(max_length=200,null=True, blank=True)
    govt_service = models.CharField(max_length=200,null=True, blank=True)

    # ...
    def __str__(self):
        return self.position

class Voluntary(models.Model):
    voluntary = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_voluntary', on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200)
    vol_from = models.DateField('from',null=True, blank=True)
    vol_to = models.DateField('to',null=True, blank=True)
    position = models.CharField(max_length=200)
    hours = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,4}$')])

    # ...
    def __str__(self):
        return self.name

class Learning(models.Model):
    learn = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_learn', on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    venue = models.CharField(max_length=200, null=True, blank=True)
    date_from = models.DateField('from',null=True, blank=True)
    date_to = models.DateField('to',null=True, blank=True)
    learning_type = models.CharField(max_length=100, null=True, blank=True)
    classification = models.CharField(max_length=100, null=True, blank=True)
    training_hours = models.CharField(max_length=255,null=True, blank=True)
    fee = models.CharField(max_length=200, null=True, blank=True)
    conducted_by = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to= "trainings/",max_length=255,null=True, blank=True)
    is_approve = models.CharField(max_length=100, default='For Review', blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)

    # ...
    def __str__(self):
        return self.title

class Other_skills(models.Model):
    ski = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_skills', on_delete=models.CASCADE,null=True, blank=True)
    skills = models.CharField(max_length=200, null=True, blank=True)
       # ...
    def __str__(self):
        return self.skills

class Other_recognitions(models.Model):
    recog = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_recognition', on_delete=models.CASCADE,null=True, blank=True)
    recognition = models.CharField(max_length=200, null=True, blank=True)
       # ...
    def __str__(self):
        return self.recognition

class Other_membership(models.Model):
    member = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_membership', on_delete=models.CASCADE,null=True, blank=True)
    member_org = models.CharField(max_length=200, null=True, blank=True)

   # ...
    def __str__(self):
        return self.member_org 

class Otherinfo(models.Model):
    otherinfo = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_otherinfo', on_delete=models.CASCADE,null=True, blank=True)
    related_third = models.CharField(max_length=200, null=True, blank=True)
    related_detail_3 = models.CharField(max_length=200, null=True, blank=True)
    related_fourth = models.CharField(max_length=200, null=True, blank=True)
    related_detail_4 = models.CharField(max_length=200, null=True, blank=True)
    admin_offense = models.CharField(max_length=200, null=True, blank=True)
    admin_offense_detail = models.CharField(max_length=200, null=True, blank=True)
    crime = models.CharField(max_length=200, null=True, blank=True)
    crime_date = models.CharField(max_length=200, null=True, blank=True)
    crime_detail = models.CharField(max_length=200, null=True, blank=True)
    convic = models.CharField(max_length=200, null=True, blank=True)
    convic_detail = models.CharField(max_length=200, null=True, blank=True)
    seperated = models.CharField(max_length=200, null=True, blank=True)
    seperated_detail = models.CharField(max_length=200, null=True, blank=True)
    candidate = models.CharField(max_length=200, null=True, blank=True)
    candidate_detail = models.CharField(max_length=200, null=True, blank=True)
    resigned = models.CharField(max_length=200, null=True, blank=True)
    resigned_detail = models.CharField(max_length=200, null=True, blank=True)
    immigrant = models.CharField(max_length=200, null=True, blank=True)
    immigrant_detail = models.CharField(max_length=200, null=True, blank=True)
    indigenous = models.CharField(max_length=200, null=True, blank=True)
    indigenous_detail = models.CharField(max_length=200, null=True, blank=True)
    disability = models.CharField(max_length=200, null=True, blank=True)
    disability_detail = models.CharField(max_length=200, null=True, blank=True)    
    disability_image = models.ImageField(upload_to= "otherinfo/",null=True, blank=True)
    soloparent = models.CharField(max_length=200, null=True, blank=True)
    soloparent_detail = models.CharField(max_length=200, null=True, blank=True)
    soloparent_image = models.ImageField(upload_to= "otherinfo/",null=True, blank=True)


class Refferences(models.Model):
    refer = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_refer', on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

    # ...
    def __str__(self):
        return self.name

class SalaryGrade(models.Model):
    salary_id = models.IntegerField(null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    step = models.IntegerField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    updated_by = models.CharField(max_length=200, null=True, blank=True)

    # ...
    def __str__(self):
        return self.salary_id

# HR Modules
class Vaccine(models.Model):
    vax = models.ForeignKey(User, db_column="user_id", related_name='pds_vax', on_delete=models.CASCADE,null=True, blank=True)
    name1 = models.CharField(max_length=200, null=True, blank=True)
    dose1 = models.CharField(max_length=200, null=True, blank=True)
    place1 = models.CharField(max_length=200, null=True, blank=True)
    date1 = models.DateField('Vax 1 Date',null=True, blank=True)
    file1 = models.ImageField(upload_to= "vaccine/",null=True, blank=True)
    name2 = models.CharField(max_length=200, null=True, blank=True)
    dose2 = models.CharField(max_length=200, null=True, blank=True)
    place2 = models.CharField(max_length=200, null=True, blank=True)
    date2 = models.DateField('Vax 2 Date',null=True, blank=True)
    file2 = models.ImageField(upload_to= "vaccine/",null=True, blank=True)
    name3= models.CharField(max_length=200, null=True, blank=True)
    dose3 = models.CharField(max_length=200, null=True, blank=True)
    place3 = models.CharField(max_length=200, null=True, blank=True)
    date3 = models.DateField('Vax 3 Date',null=True, blank=True)
    file3 = models.ImageField(upload_to= "vaccine/",null=True, blank=True)
    name4= models.CharField(max_length=200, null=True, blank=True)
    dose4 = models.CharField(max_length=200, null=True, blank=True)
    place4 = models.CharField(max_length=200, null=True, blank=True)
    date4 = models.DateField('Vax 4 Date',null=True, blank=True)
    file4 = models.ImageField(upload_to= "vaccine/",null=True, blank=True)

   # ...
    def __str__(self):
        return self.name 

# HR Trainings
class Training(models.Model):
    training = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_training', on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    venue = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField('date',null=True, blank=True)
    learning_type = models.CharField(max_length=100, null=True, blank=True)
    classification = models.CharField(max_length=100, null=True, blank=True)
    training_hours = models.IntegerField(null=True, blank=True)
    fee = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to= "trainings/",null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)


   # ...
    def __str__(self):
        return self.title 

# HR Payroll
class Payroll(models.Model):
    payroll = models.OneToOneField(User, db_column="user_id", related_name='pds_payroll', on_delete=models.CASCADE,null=True, blank=True)
    personal = models.OneToOneField(Personal, db_column="personal_id", related_name='pds_personal', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    position = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    gross = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    pay_413_1a = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class January(models.Model):
    january = models.OneToOneField(User, db_column="user_id", related_name='pds_jan', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    pay_413_1a = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class February(models.Model):
    february = models.OneToOneField(User, db_column="user_id", related_name='pds_feb', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class March(models.Model):
    march = models.OneToOneField(User, db_column="user_id", related_name='pds_march', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class April(models.Model):
    april = models.OneToOneField(User, db_column="user_id", related_name='pds_april', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class May(models.Model):
    may = models.OneToOneField(User, db_column="user_id", related_name='pds_may', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class June(models.Model):
    june = models.OneToOneField(User, db_column="user_id", related_name='pds_june', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class July(models.Model):
    july = models.OneToOneField(User, db_column="user_id", related_name='pds_july', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class August(models.Model):
    august = models.OneToOneField(User, db_column="user_id", related_name='pds_aug', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class September(models.Model):
    september = models.OneToOneField(User, db_column="user_id", related_name='pds_sep', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class October(models.Model):
    october = models.OneToOneField(User, db_column="user_id", related_name='pds_oct', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class November(models.Model):
    november = models.OneToOneField(User, db_column="user_id", related_name='pds_nov', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

    @property
    def bonus(self):
        return (Bunuses.objects.filter(Bunus_id = self.november_id).first())

class December(models.Model):
    december = models.OneToOneField(User, db_column="user_id", related_name='pds_dec', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    pay_731 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_732 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_733_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_734 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_701 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_412 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_415_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_6 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_11e = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_14 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_413_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_1a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_2a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_414_3a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_8 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_9 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_10b = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_13 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_16 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_28 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_33 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_34 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_439_35 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_146 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_148 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_801 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_149_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_711 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_749_osp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deduc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    netpay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rata = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_111_07 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_15th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_30th = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    gross = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
   
   # ...
    def __str__(self):
        return self.surname 

class Payslipstatus(models.Model):
    class Status_Payslip(models.TextChoices):
        Active = 'Active'
        Not_Active = 'Not Active'

    month = models.CharField(max_length=200,null=True, blank=True) 
    status = models.CharField(max_length=200, choices=Status_Payslip.choices,
        default=Status_Payslip.Not_Active,) 

   # ...
    def __str__(self):
        return self.month 

class Leave(models.Model):
    leave = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_leave', on_delete=models.CASCADE,null=True, blank=True)
    period = models.CharField(max_length=200, null=True, blank=True)
    particulars = models.CharField(max_length=200, null=True, blank=True)
    vacation_earned = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    vacation_wpay = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    vacation_balance = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    vacation_wopay = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    sick_earned = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    sick_wpay = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    sick_balance = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    sick_wopay = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField('created', null=True, blank=True)
    updated_by = models.CharField(max_length=200, null=True, blank=True)


    # ...
    def __str__(self):
        return self.particulars

class SPFLeave(models.Model):
    leave = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_spfleave', on_delete=models.CASCADE,null=True, blank=True)
    force = models.CharField(max_length=200)
    special = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200, null=True, blank=True)

    # ...
    def __str__(self):
        return self.updated_by

class Position(models.Model):
    position_id = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    classification = models.CharField(max_length=200)
    gcg = models.CharField(max_length=200)
    dotr = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200, null=True, blank=True)

class Signatory(models.Model):    
    name = models.CharField(max_length=200, null=True, blank=True)
    pay_designate_rate = models.CharField(max_length=200, null=True, blank=True)
    pay_designate_rate_possition = models.CharField(max_length=200, null=True, blank=True)
    pay_prepare = models.CharField(max_length=200, null=True, blank=True)
    pay_prepare_possition = models.CharField(max_length=200, null=True, blank=True)
    pay_approve = models.CharField(max_length=200, null=True, blank=True)
    pay_approve_possition = models.CharField(max_length=200, null=True, blank=True)
    updated_by = models.CharField(max_length=200, null=True, blank=True)

    # ...
    def __str__(self):
        return self.name

class NotifyTraining(models.Model):    
    notify = models.ForeignKey(Personal, db_column="personal_id", related_name='pds_notify', on_delete=models.CASCADE,null=True, blank=True)
    status = models.CharField(max_length=800, null=True, blank=True)    
    date_created = models.DateTimeField('post_date',null=True, blank=True)

    # ...
    def __str__(self):
        return self.notify

class Notifications(models.Model):    
    notify = models.CharField(max_length=800, null=True, blank=True)
    title = models.CharField(max_length=800, null=True, blank=True)
    body = models.CharField(max_length=800, null=True, blank=True)
    status = models.CharField(max_length=800, null=True, blank=True)    
    date_created = models.DateTimeField('post_date',null=True, blank=True)

    # ...
    def __str__(self):
        return self.notify

class Bonuses(models.Model):
    bonus = models.OneToOneField(User, db_column="user_id", related_name='pds_bonus', on_delete=models.CASCADE,null=True, blank=True)
    surname = models.CharField(max_length=200,null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    office = models.CharField(max_length=100,null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    mid_year_bonus = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    year_end_bonus = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cash_gift = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    patcomc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    liquidation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    
   
   # ...
    def __str__(self):
        return self.surname 

    @property
    def payroll_pay(self):
        return (Payroll.objects.filter(payroll_id = self.bonus_id).first())
        
class UnmarriedChildren(models.Model):
    child = models.ForeignKey(User, db_column="user_id", related_name='saln_child', on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    birth_date = models.DateField('birth',null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateField('created_date',null=True, blank=True)    

   # ...
    def __str__(self):
        return self.name 

    @property
    def age(self):
        if self.birth_date is None:
            return(self.birth_date)
        return int((datetime.now().date() - self.birth_date).days / 365.25)

class RealProperties(models.Model):
    real_properties = models.ForeignKey(User, db_column="user_id", related_name='saln_real', on_delete=models.CASCADE,null=True, blank=True)
    description = models.CharField(max_length=200,null=True, blank=True)
    kind = models.CharField(max_length=200,null=True, blank=True)
    location = models.CharField(max_length=200,null=True, blank=True)
    assesed_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    market_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    aquired_year = models.CharField(max_length=200,null=True, blank=True)
    aquired_mode = models.CharField(max_length=200,null=True, blank=True)
    aquired_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateField('created_date',null=True, blank=True)    

   # ...
    def __str__(self):
        return self.description 

class PersonalProperties(models.Model):
    personal_properties = models.ForeignKey(User, db_column="user_id", related_name='saln_personal', on_delete=models.CASCADE,null=True, blank=True)
    description = models.CharField(max_length=200,null=True, blank=True)
    aquired_year = models.CharField(max_length=200,null=True, blank=True)
    aquired_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateField('created_date',null=True, blank=True)    

   # ...
    def __str__(self):
        return self.description 

class Liabilities(models.Model):
    liabilities = models.ForeignKey(User, db_column="user_id", related_name='saln_liabilities', on_delete=models.CASCADE,null=True, blank=True)
    nature = models.CharField(max_length=200,null=True, blank=True)
    creditor = models.CharField(max_length=200,null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateField('created_date',null=True, blank=True)    

   # ...
    def __str__(self):
        return self.nature 

class Business(models.Model):
    business = models.ForeignKey(User, db_column="user_id", related_name='saln_business', on_delete=models.CASCADE,null=True, blank=True)
    entity_business = models.CharField(max_length=200,null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    nature = models.CharField(max_length=200,null=True, blank=True)
    date_aquired = models.CharField(max_length=100, null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateField('created_date',null=True, blank=True)    

   # ...
    def __str__(self):
        return self.entity_business 

class SalnRelative(models.Model):
    relative = models.ForeignKey(User, db_column="user_id", related_name='saln_relative', on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    relationship = models.CharField(max_length=200,null=True, blank=True)
    position = models.CharField(max_length=200,null=True, blank=True)
    agency = models.CharField(max_length=200,null=True, blank=True)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateField('created_date',null=True, blank=True)    

   # ...
    def __str__(self): 
        return self.name 


class Qrcode(models.Model):
    qr = models.ForeignKey(Personal, db_column="personal_id", related_name='file_qr', on_delete=models.CASCADE,null=True, blank=True)
    url_name = models.CharField(max_length=200, blank=True, null=True)
    emp_name = models.CharField(max_length=200, blank=True, null=True)
    unique_id = models.CharField(max_length=200, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return self.url_name

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.url_name)
        canvas = Image.new('RGB', (360, 360), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'{self.unique_id}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Caapeu(models.Model):
    caapeu = models.ForeignKey(User, db_column="user_id", related_name='user_eu', on_delete=models.CASCADE,null=True, blank=True)
    caapeu_pass = models.CharField(max_length=200)

    @property
    def UserName(self):
        return (User.objects.filter(username= self.caapeu).last())

    # ...
    def __str__(self):
        return self.caapeu

class Post(models.Model):    
    title = models.CharField(max_length=200, null=True, blank=True)
    post = models.CharField(max_length=800, null=True, blank=True)
    post_date = models.DateField('post_date',null=True, blank=True)
    file = models.FileField(upload_to= "Post/",null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    post_type = models.CharField(max_length=200, null=True, blank=True)
    ext = models.CharField(max_length=200, null=True, blank=True)
    create_by = models.CharField(max_length=200, null=True, blank=True)

    # ...
    def __str__(self):
        return self.title
    @property
    def imgs(self):
        return (MultipleImage.objects.filter(post_id= self.id).order_by('id'))

class MultipleImage(models.Model):
    post = models.ForeignKey(Post, db_column="post_id", related_name='post_up', on_delete=models.CASCADE,null=True, blank=True)
    images = models.FileField()