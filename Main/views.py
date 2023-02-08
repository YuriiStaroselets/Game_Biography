from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from Games.models import Games

def main_page(request):
	games= Games.objects.order_by("-Rate")[:8]
	return render(request, 'Main/main.html', {'games': games})
