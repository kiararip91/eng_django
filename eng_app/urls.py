from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='my-home'),
    path('2', views.homeLevelTwo, name='my-home'),
    path('3', views.homeLevelThree, name='my-home'),

]
