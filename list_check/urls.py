from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='homepage'),
    path('adding/', views.adding, name='adding'),
    path('adding/analyse/', views.analyse, name='analyse/'),
]