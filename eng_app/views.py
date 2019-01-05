from django.shortcuts import render
from . import appUtils


def home(request):
	"""
		In Context devo passare i contenuti che recupero dal Google Sheet
	"""
	word = appUtils.getWord()
	context = {
		'word' : word
	}
	return render(request, 'eng_app/home.html', context)
