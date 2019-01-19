from django.shortcuts import render
from . import appUtils
from django.http import HttpResponse
import json


def home(request):
    return render(request, 'eng_app/choose-level.html')


def startGame(request, level):
    words = appUtils.getWordFromDb(level)
    context = {
        'words': words,
        'numberOfwords': '10'
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
