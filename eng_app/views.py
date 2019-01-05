from django.shortcuts import render
from . import appUtils

#TODO: Migliorare la parametrizzazione del livello!!!
def home(request):
    word = appUtils.getWordFromDb(1)
    context = {
        'word': word
    }
    return render(request, 'eng_app/home.html', context)


def homeLevelTwo(request):
    word = appUtils.getWordFromDb(2)
    context = {
        'word': word
    }
    return render(request, 'eng_app/home.html', context)


def homeLevelThree(request):
    word = appUtils.getWordFromDb(3)
    context = {
        'word': word
    }
    return render(request, 'eng_app/home.html', context)
