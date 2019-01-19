from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='my-home'),
    path('level/<int:level>', views.startGame, name='my-home'),
    path('acronyms', views.acronyms, name='acr'),
    path('ac/type/<slug:type>', views.startAcronyms, name='acr'),
    path('update/<int:index>/<int:rightScore>/<int:wrongScore>/<int:isCorrect>', views.updateScore, name='update-score'),
]
