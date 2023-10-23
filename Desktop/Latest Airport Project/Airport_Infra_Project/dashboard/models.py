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

class Bulletin(models.Model):    
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.CharField(max_length=5000, null=True, blank=True)
    bulletin_date = models.DateField('bulletin_date',null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    create_by = models.CharField(max_length=200, null=True, blank=True)

    # ...
    def __str__(self):
        return self.title

    @property
    def BulletinImgs(self):
        return (BulletinFile.objects.filter(bulletin_id= self.id).order_by('id'))

    @property
    def BulletinComnt(self):
        return (BulletinComment.objects.filter(bulletin_id= self.id).order_by('id'))

    @property
    def BulletinAknldg(self):
        return (Aknowledge.objects.filter(bulletin_id= self.id).order_by('id'))
    

class BulletinFile(models.Model):
    bulletin = models.ForeignKey(Bulletin, db_column="bulletin_id", related_name='bulletin_file', on_delete=models.CASCADE,null=True, blank=True)
    images = models.FileField(upload_to= "Bulletin/",null=True, blank=True)
    ext = models.CharField(max_length=200, null=True, blank=True)    
    upload_date = models.DateField('upload_date',null=True, blank=True)

class Aknowledge(models.Model):
    bulletin_title = models.CharField(max_length=200, null=True, blank=True)    
    bulletin = models.ForeignKey(Bulletin, db_column="bulletin_id", related_name='bulletin_viewed',null=True, on_delete=models.DO_NOTHING, blank=True)
    aknowledge_date = models.DateTimeField('upload_date',null=True, blank=True)
    status = models.CharField(max_length=100 ,null=True, blank=True)    
    create_by = models.CharField(max_length=200, null=True, blank=True)      
    create_by_id = models.IntegerField(null=True, blank=True)

class BulletinComment(models.Model):
    comment = models.CharField(max_length=200, null=True, blank=True)    
    bulletin = models.ForeignKey(Bulletin, db_column="bulletin_id", related_name='bulletin_comment',null=True, on_delete=models.CASCADE, blank=True)
    comment_date = models.DateTimeField('upload_date',null=True, blank=True)
    create_by = models.CharField(max_length=200, null=True, blank=True)

class AiportProject(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True) 
    location = models.CharField(max_length=200, null=True, blank=True) 
    description = models.CharField(max_length=1000, null=True, blank=True)
    fund_org = models.CharField(max_length=255, null=True, blank=True)
    fund_amount = models.DecimalField(max_digits=100, decimal_places=2, default=Decimal(0.00), blank=True)
    fund_year = models.CharField(max_length=255, null=True, blank=True) 
    contract_mi = models.CharField(max_length=255, null=True, blank=True) 
    contract_contractor = models.CharField(max_length=199, null=True, blank=True)   
    contract_amount = models.DecimalField(max_digits=100, decimal_places=2, default=Decimal(0.00), blank=True)    
    contract_rev1 = models.CharField(max_length=200, null=True, blank=True)      
    contract_rev2 = models.CharField(max_length=200, null=True, blank=True)        
    duration = models.IntegerField(null=True, blank=True)    
    start = models.DateField('start',null=True, blank=True)  
    original = models.DateField('original',null=True, blank=True)     
    revised = models.DateField('revised',null=True, blank=True)  
    status_desc = models.CharField(max_length=1000, null=True, blank=True) 
    slippage = models.CharField(max_length=200, null=True, blank=True)     
    agency = models.CharField(max_length=200, null=True, blank=True)     
    status = models.CharField(max_length=1000, null=True, blank=True) 
    area = models.CharField(max_length=200, null=True, blank=True) 
    region = models.CharField(max_length=200, null=True, blank=True) 
    certificate = models.CharField(max_length=200, null=True, blank=True) 
    recouped_pay = models.CharField(max_length=200, null=True, blank=True)       
    progress = models.IntegerField(null=True, blank=True)
    created_by = models.CharField(max_length=200, null=True, blank=True)
    edited_by = models.CharField(max_length=200, null=True, blank=True)        
    date_created = models.DateTimeField('create_date',null=True, blank=True)  
    date_edited = models.DateTimeField('edit_date',null=True, blank=True)

    # @property
    # def cal_days(self):
    #     if self.start is None:
    #         return(self.birth_date)
    #     return int((datetime.now().date() - self.start).days)

class AiportProfile(models.Model):
    airportuid = models.CharField(max_length=200, null=True, blank=True) 
    name = models.CharField(max_length=200, null=True, blank=True) 
    category = models.CharField(max_length=200, null=True, blank=True)
    crit_aircraft= models.CharField(max_length=200, null=True, blank=True) 
    icao_code= models.CharField(max_length=200, null=True, blank=True) 
    designation = models.CharField(max_length=200, null=True, blank=True) 
    nehca = models.CharField(max_length=200, null=True, blank=True) 
    runway_dimension = models.CharField(max_length=200, null=True, blank=True)
    runway_surface = models.CharField(max_length=200, null=True, blank=True) 
    runway_obstacles = models.CharField(max_length=200, null=True, blank=True) 
    runway_remarks = models.CharField(max_length=200, null=True, blank=True) 
    taxiway_dimension = models.CharField(max_length=200, null=True, blank=True) 
    taxiway_surface = models.CharField(max_length=200, null=True, blank=True) 
    taxiway_num = models.IntegerField(null=True, blank=True)
    taxiway_description = models.CharField(max_length=200, null=True, blank=True) 
    apron_dimension = models.CharField(max_length=200, null=True, blank=True)  
    apron_surface = models.CharField(max_length=200, null=True, blank=True)        
    apron_num = models.CharField(max_length=200, null=True, blank=True)
    ptb_dimension = models.CharField(max_length=200, null=True, blank=True) 
    ptb_aircon = models.CharField(max_length=200, null=True, blank=True) 
    ptb_toilet = models.CharField(max_length=200, null=True, blank=True) 
    tower = models.CharField(max_length=200, null=True, blank=True)  
    com_flight = models.CharField(max_length=200, null=True, blank=True)    
    note = models.CharField(max_length=200, null=True, blank=True)     
    profile_photo = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_photo.png", blank=True)
    profile_runway = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_runway.png", blank=True)
    profile_apron = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_apron.png", blank=True)
    profile_ptb = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_ptb.png", blank=True)
    profile_taxiway = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_ptb.png", blank=True)
    profile_photo_1 = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_photo.png", blank=True)
    profile_runway_1 = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_runway.png", blank=True)
    profile_apron_1 = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_apron.png", blank=True)
    profile_ptb_1 = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_ptb.png", blank=True)
    profile_taxiway_1 = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_ptb.png", blank=True)
    profile_photo_2 = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_photo.png", blank=True)
    profile_runway_2 = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_runway.png", blank=True)
    profile_apron_2 = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_apron.png", blank=True)
    profile_ptb_2 = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_ptb.png", blank=True)
    profile_taxiway_2 = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_ptb.png", blank=True)
    created_by = models.CharField(max_length=200, null=True, blank=True) 
    edited_by = models.CharField(max_length=200, null=True, blank=True)        
    date_created = models.DateTimeField('create_date',null=True, blank=True)  
    date_edited = models.DateTimeField('edit_date',null=True, blank=True)    
    operation_hours = models.CharField(max_length=200, null=True, blank=True)      
    firetruck = models.CharField(max_length=200, null=True, blank=True)     
    nav_iads = models.CharField(max_length=200, null=True, blank=True)        
    night_rating = models.CharField(max_length=200, null=True, blank=True)  
    airport_contact = models.CharField(max_length=200, null=True, blank=True)    
    airport_manager = models.CharField(max_length=200, null=True, blank=True)  
    airport_manager_contact = models.CharField(max_length=200, null=True, blank=True)  
    airport_email = models.CharField(max_length=200, null=True, blank=True)  
    area_center = models.CharField(max_length=200, null=True, blank=True)  





    