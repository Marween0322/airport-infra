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
from .models import AiportProject, AiportProfile
from .forms import AiportProjectForm, AiportProfileForm
from django.views.decorators.clickjacking import xframe_options_exempt
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

@login_required 
def Airports(request):
    
    if request.user.groups.filter(name='odg'):
        return render(request, 'dashboard/airports/index4.html') 
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')

@xframe_options_exempt
def AirportMap(request):    
    return render(request, 'dashboard/airports/index.html') 

@xframe_options_exempt
def AreaCenter1(request):    
    laoag = AiportProfile.objects.get(airportuid__iexact = "Laoag1")    
    vigan = AiportProfile.objects.get(airportuid__iexact = "Vigan1")  
    baguio = AiportProfile.objects.get(airportuid__iexact = "Baguio1")  
    lingayen = AiportProfile.objects.get(airportuid__iexact = "Lingayen1")  
    rosales = AiportProfile.objects.get(airportuid__iexact = "Rosales1")  
    sanfe = AiportProfile.objects.get(airportuid__iexact = "SanFernando1")

    context = { 'laoag': laoag ,'vigan': vigan ,'baguio': baguio ,'lingayen': lingayen ,'rosales': rosales ,'sanfe': sanfe , }
    return render(request, 'dashboard/airports/area1.html', context)


@xframe_options_exempt
def AreaCenter2(request):
    tuguegarao = AiportProfile.objects.get(airportuid__iexact = "Tuguegarao2")    
    basco = AiportProfile.objects.get(airportuid__iexact = "Basco2")  
    cauayan = AiportProfile.objects.get(airportuid__iexact = "Cauayan2")  
    bagabag = AiportProfile.objects.get(airportuid__iexact = "Bagabag2")  
    itbayat = AiportProfile.objects.get(airportuid__iexact = "Itbayat2")  
    palanan = AiportProfile.objects.get(airportuid__iexact = "Palanan2")

    context = { 'tuguegarao': tuguegarao, 'cauayan': cauayan, 'basco': basco, 'bagabag': bagabag, 'itbayat': itbayat, 'palanan' : palanan}
    return render(request, 'dashboard/airports/area2.html', context)

@xframe_options_exempt
def AreaCenter3(request):
    sanjose = AiportProfile.objects.get(airportuid__iexact = "SanJose3")    
    sangley = AiportProfile.objects.get(airportuid__iexact = "Sangley3")  
    romblon = AiportProfile.objects.get(airportuid__iexact = "Romblon3")  
    marinduque = AiportProfile.objects.get(airportuid__iexact = "Marinduque3")  
    plaridel = AiportProfile.objects.get(airportuid__iexact = "Plaridel3")  
    baler = AiportProfile.objects.get(airportuid__iexact = "Baler3")
    iba = AiportProfile.objects.get(airportuid__iexact = "Iba3")    
    alabat = AiportProfile.objects.get(airportuid__iexact = "Alabat3")  
    jomalig = AiportProfile.objects.get(airportuid__iexact = "Jomalig3")  
    lubang = AiportProfile.objects.get(airportuid__iexact = "Lubang3")  
    calapan = AiportProfile.objects.get(airportuid__iexact = "Calapan3")  
    mamburao = AiportProfile.objects.get(airportuid__iexact = "Mamburao3")
    pinamalayan = AiportProfile.objects.get(airportuid__iexact = "Pinamalayan3")    
    wasig = AiportProfile.objects.get(airportuid__iexact = "Wasig3")  
    casiguran = AiportProfile.objects.get(airportuid__iexact = "Casiguran3")  

    context = { 'sanjose': sanjose, 'sangley': sangley, 'romblon': romblon, 'marinduque': marinduque, 'plaridel': plaridel, 'baler' : baler, 'iba': iba,'alabat': alabat,'jomalig': jomalig,'lubang': lubang,'calapan': calapan,'mamburao': mamburao,'pinamalayan': pinamalayan,'wasig': wasig,'casiguran': casiguran}
    return render(request, 'dashboard/airports/area3.html', context)

@xframe_options_exempt
def AreaCenter4(request):

    puerto = AiportProfile.objects.get(airportuid__iexact = "PuertoPrincesa4")    
    sanvicente = AiportProfile.objects.get(airportuid__iexact = "SanVicente4") 
    cuyo = AiportProfile.objects.get(airportuid__iexact = "Cuyo4")    
    busuanga = AiportProfile.objects.get(airportuid__iexact = "Busuanga4")   

    context = { 'puerto': puerto, 'sanvicente': sanvicente,'cuyo': cuyo, 'busuanga': busuanga}
    return render(request, 'dashboard/airports/area4.html', context)

@xframe_options_exempt
def AreaCenter5(request):

    legazpi = AiportProfile.objects.get(airportuid__iexact = "Legazpi5")    
    naga = AiportProfile.objects.get(airportuid__iexact = "Naga5")  
    virac = AiportProfile.objects.get(airportuid__iexact = "Virac5") 
    masbate = AiportProfile.objects.get(airportuid__iexact = "Masbate5")  
    daet = AiportProfile.objects.get(airportuid__iexact = "Daet5") 
    bacon = AiportProfile.objects.get(airportuid__iexact = "Bacon5") 
    bulan = AiportProfile.objects.get(airportuid__iexact = "Bulan5") 
    context = { 'legazpi': legazpi, 'naga': naga, 'virac': virac, 'masbate': masbate, 'daet': daet, 'bacon':bacon, 'bulan': bulan}
    
    return render(request, 'dashboard/airports/area5.html',context)

@xframe_options_exempt
def AreaCenter6(request):
    iloilo = AiportProfile.objects.get(airportuid__iexact = "Iloilo6") 
    kalibo = AiportProfile.objects.get(airportuid__iexact = "Kalibo6") 
    bacolod = AiportProfile.objects.get(airportuid__iexact = "Bacolod-Silay6")  
    roxas = AiportProfile.objects.get(airportuid__iexact = "Roxas6")  
    antique = AiportProfile.objects.get(airportuid__iexact = "Antique6")  
    caticlan = AiportProfile.objects.get(airportuid__iexact = "Caticlan6")  

    context = { 'iloilo':iloilo, 'kalibo':kalibo, 'bacolod':bacolod, 'roxas':roxas, 'antique':antique, 'caticlan':caticlan}
    return render(request, 'dashboard/airports/area6.html', context)

@xframe_options_exempt
def AreaCenter7(request):

    bohol = AiportProfile.objects.get(airportuid__iexact = "Bohol-Panglao7")
    dumaguete = AiportProfile.objects.get(airportuid__iexact = "Dumaguete7")  
    siquijor = AiportProfile.objects.get(airportuid__iexact = "Siquijor7")  
    ubay = AiportProfile.objects.get(airportuid__iexact = "Ubay7")  
    bantayan = AiportProfile.objects.get(airportuid__iexact = "Bantayan7")    
    
    context = {'bohol':bohol, 'dumaguete':dumaguete, 'siquijor':siquijor, 'ubay':ubay, 'bantayan':bantayan}
    return render(request, 'dashboard/airports/area7.html', context)

@xframe_options_exempt
def AreaCenter8(request):

    tacloban = AiportProfile.objects.get(airportuid__iexact = "Tacloban8") 
    calbayog = AiportProfile.objects.get(airportuid__iexact = "Calbayog8") 
    catarman = AiportProfile.objects.get(airportuid__iexact = "Catarman8")  
    ormoc = AiportProfile.objects.get(airportuid__iexact = "Ormoc8")  
    maasin = AiportProfile.objects.get(airportuid__iexact = "Maasin8")  
    borongan = AiportProfile.objects.get(airportuid__iexact = "Borongan8") 
    biliran = AiportProfile.objects.get(airportuid__iexact = "Biliran8") 
    guiuan = AiportProfile.objects.get(airportuid__iexact = "Guiuan8") 
    hilongos = AiportProfile.objects.get(airportuid__iexact = "Hilongos8") 
    catbalogan = AiportProfile.objects.get(airportuid__iexact = "Catbalogan8")  

    context= { 'tacloban':tacloban, 'calbayog':calbayog, 'catarman':catarman, 'ormoc':ormoc, 'maasin':maasin, 'borongan':borongan, 'biliran':biliran, 'guiuan':guiuan, 'hilongos':hilongos, 'catbalogan':catbalogan} 
    return render(request, 'dashboard/airports/area8.html', context)

@xframe_options_exempt
def AreaCenter9(request):

    pagadian = AiportProfile.objects.get(airportuid__iexact = "Pagadian9")
    zamboanga = AiportProfile.objects.get(airportuid__iexact = "Zamboanga9") 
    dipolog = AiportProfile.objects.get(airportuid__iexact = "Dipolog9") 
    sanga_sanga = AiportProfile.objects.get(airportuid__iexact = "Sanga-Sanga9") 
    jolo = AiportProfile.objects.get(airportuid__iexact = "Jolo9")  
    siocon = AiportProfile.objects.get(airportuid__iexact = "Siocon9") 
    ipil = AiportProfile.objects.get(airportuid__iexact = "Ipil9") 
    liloy = AiportProfile.objects.get(airportuid__iexact = "Liloy9") 
    cagayan_de_sulu = AiportProfile.objects.get(airportuid__iexact = "Cagayan_de_Sulu9") 

    context = { 'pagadian':pagadian, 'zamboanga':zamboanga, 'dipolog':dipolog, 'sanga_sanga':sanga_sanga, 'jolo':jolo, 'siocon':siocon, 'ipil':ipil, 'liloy':liloy, 'cagayan_de_sulu':cagayan_de_sulu}
    return render(request, 'dashboard/airports/area9.html', context)

@xframe_options_exempt
def AreaCenter10(request):
    laguindingan = AiportProfile.objects.get(airportuid__iexact = "Laguindingan10")    
    ozamis = AiportProfile.objects.get(airportuid__iexact = "Ozamis10")  
    camiguin = AiportProfile.objects.get(airportuid__iexact = "Camiguin10")  
    iligan = AiportProfile.objects.get(airportuid__iexact = "Iligan10")  
    malabang = AiportProfile.objects.get(airportuid__iexact = "Malabang10")  
    wao = AiportProfile.objects.get(airportuid__iexact = "Wao10")

    context = { 'laguindingan': laguindingan, 'ozamis': ozamis, 'camiguin': camiguin, 'iligan': iligan, 'malabang': malabang, 'wao' : wao}
    return render(request, 'dashboard/airports/area10.html', context)

@xframe_options_exempt
def AreaCenter11(request):

    davao = AiportProfile.objects.get(airportuid__iexact = "Davao11")
    generalsantos = AiportProfile.objects.get(airportuid__iexact = "GenSan11")
    cotabato = AiportProfile.objects.get(airportuid__iexact = "Cotabato11")
    mati = AiportProfile.objects.get(airportuid__iexact = "Mati11")
    mlang = AiportProfile.objects.get(airportuid__iexact = "Mlang11")
    allah = AiportProfile.objects.get(airportuid__iexact = "Allah11")

    context = {'davao':davao, 'generalsantos':generalsantos, 'cotabato':cotabato, 'mati':mati, 'mlang':mlang, 'allah':allah}
    return render(request, 'dashboard/airports/area11.html',context)

@xframe_options_exempt
def AreaCenter12(request):

    butuan = AiportProfile.objects.get(airportuid__iexact = "Butuan12")
    siargao = AiportProfile.objects.get(airportuid__iexact = "Siargao12")
    surigao = AiportProfile.objects.get(airportuid__iexact = "Surigao12")
    tandag = AiportProfile.objects.get(airportuid__iexact = "Tandag12")
    bislig = AiportProfile.objects.get(airportuid__iexact = "Bislig12")

    context = { 'butuan':butuan, 'siargao':siargao, 'surigao':surigao, 'tandag':tandag, 'bislig':bislig}

    return render(request, 'dashboard/airports/area12.html', context)







# ADMIN Side
@login_required 
def AirportList(request):

    if request.user.groups.filter(name='adms'):
        airports = AiportProfile.objects.all().order_by('name')
        return render(request, 'dashboard/airports/admin/airports.html', {'airports': airports})  
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')    

@login_required 
def AirportEdit(request, id):
    if request.user.groups.filter(name='adms'):
        airport = AiportProfile.objects.get( id= id)
        categorylist = ['International', 'Principal Class I', 'Principal Class II', 'Community'] 
        return render(request, 'dashboard/airports/admin/airport_edit.html', {'airport': airport, 'categorylist': categorylist})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')     

@login_required 
def AirportUpdate(request, id):
    if request.user.groups.filter(name='adms'):
        airport = AiportProfile.objects.get( id= id)

        if request.POST:
            form = AiportProfileForm(request.POST, request.FILES, instance=airport)
            if request.FILES.get('profile_photo'):
                file_check1 = 'True'
            else:
                file_check1 = 'False'

            if request.FILES.get('profile_runway'):
                file_check2 = 'True'
            else:
                file_check2 = 'False'

            if request.FILES.get('profile_apron'):
                file_check3 = 'True'
            else:
                file_check3 = 'False'

            if request.FILES.get('profile_ptb'):
                file_check4= 'True'
            else:
                file_check4 = 'False'

            if form.is_valid():
                    instance = form.save(commit=False)
                    instance.id = id
                    if file_check1 == 'True' :
                        instance.profile_photo = request.FILES['profile_photo']
                    else:
                        instance.profile_photo = airport.profile_photo
                    if file_check2 == 'True' :
                        instance.profile_runway = request.FILES['profile_runway']
                    else:
                        instance.profile_runway = airport.profile_runway
                    if file_check3 == 'True' :
                        instance.profile_apron = request.FILES['profile_apron']
                    else:
                        instance.profile_apron = airport.profile_apron
                    if file_check4 == 'True' :
                        instance.profile_ptb = request.FILES['profile_ptb']
                    else:
                        instance.profile_ptb = airport.profile_ptb
                    instance.edited_by = request.user.username
                    instance.date_edited = datetime.now()   
                    instance.save()
                    return redirect('/dashboard/airportlist')
            return render(request, 'dashboard/airports/admin/airport_edit.html', {'airport': airport}) 

        return render(request, 'dashboard/airports/admin/airport_edit.html', {'airport': airport}) 
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds') 

@login_required
def SearchAerodrome(request):
    value_aerodrome = request.POST['search_airport']    
    area = request.POST['search_area']      
    airports = AiportProfile.objects.all().order_by('name')

    if area:
            airports = airports.filter(area_center=area)
    else:
            airports = airports.filter(name__icontains=value_aerodrome)

    context = {'airports':airports , 'area':area, 'value_aerodrome':value_aerodrome}
    if request.user.groups.filter(name='odg'):
        return render(request,"dashboard/airports/admin/airports.html", context) 
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')  

@login_required
def SearchAerodromeDashboard(request):
    value_aerodrome = request.POST['search_airport']    
    area = request.POST['search_area']      
    aerodrome = AiportProfile.objects.all().order_by('name')

    if area:
            aerodrome = aerodrome.filter(area_center=area)
    else:
            aerodrome = aerodrome.filter(Q(name__icontains=value_aerodrome)|Q(category__icontains=value_aerodrome))

    context = {'aerodrome':aerodrome , 'area':area, 'value_aerodrome':value_aerodrome}
    if request.user.groups.filter(name='odg'):
        return render(request,"dashboard/airports/search.html", context) 
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')  

@login_required
def AerodromeProfile(request, name):     
    data = AiportProfile.objects.get(airportuid=name)

    context = {'data':data}
    if request.user.groups.filter(name='odg'):
        return render(request,"dashboard/airports/profile.html", context) 
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds')  

     

@login_required 
def addAirport(request):   

    if request.user.groups.filter(name='adms'):
        categorylist = ['International', 'Principal Class I', 'Principal Class II', 'Community'] 
        if request.method == "POST":    
            form = AiportProfileForm(request.POST)
            if form.is_valid():
                try:
                    today = datetime.now()
                    form.save()
                    instance = form.save(commit=False)
                    instance.created_by = request.user.first_name + " " + request.user.first_name
                    instance.date_created = today
                    instance.save()
                    return redirect('/dashboard/airportlist')
                except: 
                    print(form)
                    print("Invalid Form")
                    print(form.errors)
                    messages.success(request, 'Submit error!.')
                    return render(request, 'dashboard/airports/admin/airport_add.html', {'form': form ,'categorylist': categorylist})
            else:
                print(form)
                print("Invalid Form")
                print(form.errors)
                messages.success(request, 'Submit error!.')
                return render(request, 'dashboard/airports/admin/airport_add.html', {'form': form ,'categorylist': categorylist})
        form = AiportProfileForm(request.POST)
        return render(request, 'dashboard/airports/admin/airport_add.html', {'form': form ,'categorylist': categorylist})
    else:
        messages.success(request, 'Unauthorized Access')
        return redirect('/pds') 

     
