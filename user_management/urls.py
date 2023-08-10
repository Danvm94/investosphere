from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.registration_view, name='register'),
]
