from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('1', views.overview, name='overview')
]
