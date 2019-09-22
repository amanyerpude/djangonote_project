from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='note-home'),
    path('about/', views.about, name='note-about'),
]
