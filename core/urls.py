from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
] 