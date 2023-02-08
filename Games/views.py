from django.shortcuts import render
from django.views.generic import DetailView
from django.db.models import Q
from .models import Games

def game_page(request):
	search_query = request.GET.get('search', '')
	if search_query:
		games= Games.objects.filter(Q(title__icontains=search_query) | Q(Creators__icontains=search_query))
	else:
		games= Games.objects.order_by("-date")
	return render(request, 'Games/games.html', {'games': games})


class  GamesDetailView(DetailView):
	model = Games
	template_name = 'Games/game.html'
	context_object_name = 'games'
		
		