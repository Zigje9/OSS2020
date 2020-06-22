from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vuenote import views

urlpatterns = [
    path('notes/', views.NoteView.as_view())
]