from django.conf.urls import path
from drones import views 
 
 
urlpatterns = [ 
    path(r'^drone-categories/$',  
        views.DroneCategoryList.as_view(),  
        name=views.DroneCategoryList.name), 
    path(r'^drone-categories/(?P<pk>[0-9]+)$',  
        views.DroneCategoryDetail.as_view(), 
        name=views.DroneCategoryDetail.name), 
    path(r'^drones/$',  
        views.DroneList.as_view(), 
        name=views.DroneList.name), 
    path(r'^drones/(?P<pk>[0-9]+)$',  
        views.DroneDetail.as_view(), 
        name=views.DroneDetail.name), 
    path(r'^pilots/$',  
        views.PilotList.as_view(), 
        name=views.PilotList.name), 
    path(r'^pilots/(?P<pk>[0-9]+)$',  
        views.PilotDetail.as_view(), 
        name=views.PilotDetail.name), 
    path(r'^competitions/$',  
        views.CompetitionList.as_view(), 
        name=views.CompetitionList.name), 
    path(r'^competitions/(?P<pk>[0-9]+)$',  
        views.CompetitionDetail.as_view(), 
        name=views.CompetitionDetail.name), 
    path(r'^$', 
        views.ApiRoot.as_view(), 
        name=views.ApiRoot.name), 
    ]