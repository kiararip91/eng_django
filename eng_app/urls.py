from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='my-home'),
    path('level/<int:level>', views.startGame, name='my-home'),
    path('acronymus', views.acronymus, name='acr'),
    path('update/<int:index>/<int:rightScore>/<int:wrongScore>/<int:isCorrect>', views.updateScore, name='update-score'),

]
