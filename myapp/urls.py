from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personal_info/', views.personal_info, name='personal_info'),
    path('description/', views.description, name='description'),
    path('contact/', views.contact, name='contact'),
]