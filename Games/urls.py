from django.urls import path
from . import views

urlpatterns = [
    path('',views.game_page, name="game_page_url" ),
    path('<int:pk>', views.GamesDetailView.as_view(), name = 'games-detail')
]