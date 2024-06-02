import os
from django.shortcuts import render
from .models import Voting
from .forms import VotingForm

def index(request):
	if request.method == 'POST':
		voice = request.POST.get('voice')
		if voice == 'True':
			voting_form = VotingForm({'voice': True})
		else:
			voting_form = VotingForm({'voice': False})
		
		if voting_form.is_valid():
			voting_form.save()
			return redirect('index')
	else:
		voting_form = VotingForm()
	
	return render(request, 'vote/index.html', {'voting_form': voting_form})


def about(request):
	return render(request, 'vote/about.html')
	
def howwas(request):
	return render(request, 'vote/howwas.html')