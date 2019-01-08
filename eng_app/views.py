from django.shortcuts import render
from . import appUtils
from django.http import HttpResponse
import json

# TODO: Migliorare la parametrizzazione del livello!!!


def home(request):
    word = appUtils.getWordFromDb(1)
    context = {
        'word': word
    }
    return render(request, 'eng_app/word.html', context)


def homeLevelTwo(request):
    word = appUtils.getWordFromDb(2)
    context = {
        'word': word
    }
    return render(request, 'eng_app/word.html', context)


def homeLevelThree(request):
    word = appUtils.getWordFromDb(3)
    context = {
        'word': word
    }
    return render(request, 'eng_app/word.html', context)


def updateScore(request, index, rightScore, wrongScore, isCorrect=1):
    host = request.get_host()

    if 'localhost' or '127.0.0.1' in host:
        return HttpResponse(appUtils.updateScore(index, rightScore, wrongScore, isCorrect))
    else:
        return HttpResponse("not allowed")


def acronymus(request):
    acronymus = appUtils.getAcronymusFromDb()
    context = {
        'acronymus': acronymus
    }
    return render(request, 'eng_app/acronymus.html', context)
