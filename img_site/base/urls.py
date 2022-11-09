from django.urls import path 
from . import views


app_name = 'base'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo1'),
    path('add/',views.addPhoto, name='add'),
]

