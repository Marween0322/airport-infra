from django.urls import path, re_path
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings

from . import views, AirportsViews, projectsViews


app_name = 'dashboard' 
urlpatterns = [ 
    # Dashboard Bulletin 
    path('bulletin',views.BulletinHome,name='bulletin'),
    path('bulletinCreate',views.BulletinCreate,name='bulletinCreate'),    
    path('bulletinaknldg/<int:id>',views.Bulletin_Aknldg,name='bulletinaknldg'),    
    path('bulletincomment/<int:id>',views.Bulletin_Comment,name='bulletincomment'),    
    path('acknowledge',views.Acknowledge,name='acknowledge'),
    path('bulletinShow/<int:id>',views.Bulletin_Post,name='bulletinShow'),   
    
    # Airport Profile
        # Seach from Admin
    path('aerodrome_search',AirportsViews.SearchAerodrome, name="aerodrome_search"), 
        # Search from Dashboard    
    path('aerodrome_search_dashboard',AirportsViews.SearchAerodromeDashboard, name="aerodrome_search_dashboard"),
        # show Aerodrome profile    
    path('aerodrome_profile/<str:name>',AirportsViews.AerodromeProfile, name='aerodrome_profile'),  
    path('airports',AirportsViews.Airports,name='airports'),
    path('airportmap',AirportsViews.AirportMap,name='airportmap'),
    path('areaC1',AirportsViews.AreaCenter1,name='areaC1'),
    path('areaC2',AirportsViews.AreaCenter2,name='areaC2'),
    path('areaC3',AirportsViews.AreaCenter3,name='areaC3'),
    path('areaC4',AirportsViews.AreaCenter4,name='areaC4'),
    path('areaC5',AirportsViews.AreaCenter5,name='areaC5'),
    path('areaC6',AirportsViews.AreaCenter6,name='areaC6'),
    path('areaC7',AirportsViews.AreaCenter7,name='areaC7'),
    path('areaC8',AirportsViews.AreaCenter8,name='areaC8'),
    path('areaC9',AirportsViews.AreaCenter9,name='areaC9'),
    path('areaC10',AirportsViews.AreaCenter10,name='areaC10'),
    path('areaC11',AirportsViews.AreaCenter11,name='areaC11'),
    path('areaC12',AirportsViews.AreaCenter12,name='areaC12'),

    # Airport Profile Admin
    path('airport_add',AirportsViews.addAirport,name='airport_add'),
    path('airportlist',AirportsViews.AirportList,name='airportlist'),    
    path('airportedit/<int:id>', AirportsViews.AirportEdit, name= 'airportedit'),  
    path('airportupdate/<int:id>', AirportsViews.AirportUpdate, name= 'airportupdate'),  

    # Airport Projects  
    path('project_search',projectsViews.SearchProject), 
    path('airportproject/<str:name>',projectsViews.Project), 
    path('view/<int:id>',projectsViews.viewProject),
    path('',projectsViews.dashView),   

    path('caap',projectsViews.CAAP),  
    path('dotr',projectsViews.DOTr), 
    path('complete',projectsViews.complete_projects , name= 'complete'),
    path('ongoing',projectsViews.ongoing_projects , name= 'ongoing'),
    path('procurement',projectsViews.procurement_projects , name= 'procurement'),
    # Projects CRUD
    path('add_project',projectsViews.addProject ),   
    path('edit/<int:id>', projectsViews.edit),  
    path('project_update/<int:id>', projectsViews.update),  
    path('delete/<int:id>', projectsViews.destroy),   


  
    # Media Url Pattern    
    re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], views.protected_serve, {'document_root': settings.MEDIA_ROOT}),
] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
