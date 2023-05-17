from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('author/', views.author, name='author'),
        path('create/', views.create, name='create'),
        path('details/', views.details, name='details'),
        path('explore/', views.explore, name='explore'),


]
