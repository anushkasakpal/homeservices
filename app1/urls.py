from django.urls import path
from . import views

urlpatterns = [
    path('uv/', views.adduser, name='add'),
    path('sv/', views.showView, name='show'),
    path('up/<int:pk>/', views.updateView, name='update'),
    path('dl/<int:pk>/', views.deleteView, name='delete'),
    path('', views.home, name='home'),
    path('el/', views.electrician, name='electrician'),
    path('el/', views.plumber, name='plumber'),
    path('el/', views.cleaner, name='cleaner'),
    path('el/', views.carpenter, name='carpenter'),
    path('el/', views.painter, name='painter'),
    path('el/', views.welder, name='welder'),
    path('sf/', views.success, name='successful'),
    path('au/', views.aboutus, name='aboutus'),
    path('cu/', views.contactus, name='contactus'),
]