from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # default authentication URL patterns
    path('', include('django.contrib.auth.urls')),
]
