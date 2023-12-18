from django.urls import path 
from . import models 

urlpatterns = [ 
    path('form/', models.Booking, name='Booking'), 

] 