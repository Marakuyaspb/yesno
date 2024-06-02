import os
from django.utils import timezone
from django.shortcuts import render
from .forms import VotingForm


def index(request):
	if request.method == 'POST':
		voice = request.POST.get('voice')
		create = timezone.now()

		voting_form = VotingForm({'voice': voice, 'create': create})

		if voting_form.is_valid():
			instance = voting_form.save(commit=False)
			instance.voice = voice
			instance.create = create
			instance.save()
			print("Form saved successfully!")
		else:
			print("Form validation errors:", voting_form.errors)
	else:
		voting_form = VotingForm()
	
	return render(request, 'vote/index.html', {'voting_form': voting_form})


def about(request):
	return render(request, 'vote/about.html')
	
def howwas(request):
	return render(request, 'vote/howwas.html')