from django.urls import path
from . import views

urlpatterns = [
    path('bk/', views.book, name='book'),
    path('ss/', views.showServicemen, name='showservicemen'),
    path('as/', views.addServicemen, name='addservicemen'),
    path('et/', views.showElectrician, name='showelectrician'),
    path('pl/', views.showPlumber, name='showplumber'),
    path('cn/', views.showCleaner, name='showcleaner'),
    path('cp/', views.showCarpenter, name='showcarpenter'),
    path('pt/', views.showPainter, name='showpainter'),
    path('wd/', views.showWelder, name='showwelder'),
    path('ar/', views.adminregisterView, name='adminregister'),
    path('al/', views.adminloginView, name='adminlog'),
    path('alt/', views.adminlogoutView, name='adminlogout'),
    ]