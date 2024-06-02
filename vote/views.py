import os
from django.shortcuts import render

def index(request):
	return render(request, 'vote/index.html')
def about(request):
	return render(request, 'vote/about.html')
def howwas(request):
	return render(request, 'vote/howwas.html')