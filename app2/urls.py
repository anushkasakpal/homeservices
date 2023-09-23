from django.urls import path
from . import views


urlpatterns = [
    path('rv/', views.registerView, name='register_url'),
    path('log/', views.loginView, name='log_url'),
    path('lot/', views.loginView, name='logout_url')
]