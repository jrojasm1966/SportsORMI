from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		# 1 todas las ligas de beisbol 
		# "leagues": League.objects.filter(sport='Baseball'),
		# 2 todas las ligas de mujeres
		# "leagues": League.objects.filter(name__icontains='Womens'),
		# 3 todas las ligas donde el deporte es cualquier tipo de hockey
		# "leagues": League.objects.filter(sport__icontains='Hockey'),
		# 4 todas las ligas donde el deporte no sea football
		# "leagues": League.objects.exclude(sport='Football'),
		# 5 todas las ligas que se llaman conferencias(Conference)
		# "leagues": League.objects.filter(name__icontains='Conference'),
		# 6 todas las ligas de la region atlantica
		# "leagues": League.objects.filter(name__icontains='Atlantic'),
		"leagues": League.objects.filter(name__icontains='Atlantic'),
		# 7 todos los equipos con sede en Dallas
		# "teams": Team.objects.filter(location='Dallas'),
		# 8 todos los equipos nombrados los raptors
		# "teams": Team.objects.filter(team_name='Raptors'),
		# 9 todos los cuya ubicacion incluya City
		# "teams": Team.objects.filter(location__icontains='City'),
		# 10 todos los equipos cuyos nombres comienzen con T
		# "teams": Team.objects.filter(team_name__startswith='T'),
		# 11 todos los equipos, ordenados alfabeticamente por ubicacion
		# "teams": Team.objects.order_by('location'),
		# 12 todos los equipos, ordenados por nombre de equipo en orden alfabetico inverso
		"teams": Team.objects.order_by('-team_name'),
		# 13 cada jugador con apellido Cooper
		# "players": Player.objects.filter(last_name='Cooper'),
		# 14 cada jugador con nombre Joshua
		# "players": Player.objects.filter(first_name='Joshua'),
		# 15 todos los jugadores con el apellido Cooper excepto aquellos de nombre Joshua
		# "players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),
		# 16 todos los jugadores con el nombre Alexander o Wyatt
		"players": Player.objects.filter(first_name='Joshua')|Player.objects.filter(first_name='Wyatt'),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")