from django.contrib import admin
from django.urls import path
from search_pages_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('image/', views.image_search, name="image"),
    path('advanced/', views.advanced_search, name="advanced"),
]