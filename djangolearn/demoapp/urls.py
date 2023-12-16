from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('home',views.home),
    #mapping urls with params
    path('dishes/<str:dish>',views.menuitems),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 

] 