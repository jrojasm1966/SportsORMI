from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count
from . import team_maker

def index(request):
	context = {
		# Queries ORM de Origen
		#"leagues": League.objects.all(),
		#"teams": Team.objects.all(),
		#"players": Player.objects.all(),
  
		# Queries ORM de Sports ORM I
		# 1 todas las ligas de beisbol 
		#"leagues": League.objects.filter(sport='Baseball'),
		# 2 todas las ligas de mujeres
		 "leagues": League.objects.filter(name__icontains='Womens'),
		# 3 todas las ligas donde el deporte es cualquier tipo de hockey
		# "leagues": League.objects.filter(sport__icontains='Hockey'),
		# 4 todas las ligas donde el deporte no sea football
		# "leagues": League.objects.exclude(sport='Football'),
		# 5 todas las ligas que se llaman conferencias(Conference)
		# "leagues": League.objects.filter(name__icontains='Conference'),
		# 6 todas las ligas de la region atlantica
		# "leagues": League.objects.filter(name__icontains='Atlantic'),
		#"leagues": League.objects.filter(name__icontains='Atlantic'),
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
		#"teams": Team.objects.order_by('-team_name'),
		# 13 cada jugador con apellido Cooper
		# "players": Player.objects.filter(last_name='Cooper'),
		# 14 cada jugador con nombre Joshua
		# "players": Player.objects.filter(first_name='Joshua'),
		# 15 todos los jugadores con el apellido Cooper excepto aquellos de nombre Joshua
		# "players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),
		# 16 todos los jugadores con el nombre Alexander o Wyatt
		#"players": Player.objects.filter(first_name='Joshua')|Player.objects.filter(first_name='Wyatt'),

		# Queries ORM de Sports ORM II
		# 1 todos los equipos de la Atlantic Soccer Conference
		# "teams": Team.objects.filter(league=League.objects.filter(name="Atlantic Soccer Conference")),
		# 2 todos los jugadores en los boston penquins
		# "players": Player.objects.filter(curr_team=Team.objects.filter(team_name="Penguins", location="Boston")),
		# 3 todos los jugadores en la international Collegiate baseball conference
		 "players": Player.objects.filter(curr_team__league__name = "International Collegiate Baseball Conference"),
		# 4 todos los jugadores en la conferencia Americana de Futbol Amateur con el apellido Lopez
		# "players": Player.objects.filter(curr_team__league__name = "American Conference of Amateur Football", last_name = "Lopez"),
		# 5 todos los jugadores de futbol
		# "players": Player.objects.filter(curr_team__league__sport = "Football"),
		# 6 todos los equipos con un jugador llamado Sophia
		 "teams": Team.objects.filter(curr_players__first_name="Sophia"),
  		# 7 todas las ligas con un jugador llamado Sophia
		#"leagues": League.objects.filter(teams__curr_players__first_name = "Sophia"),
		# 8 todos con el apellido Flores que no jugan para los washington roughriders
		# "players": Player.objects.filter(last_name='Flores').exclude(curr_team__team_name = 'Roughriders', curr_team__location = 'Washington'),
		# 9 todos los equipos, pasados y presentes con los que Samuel Evans ha jugado
		#"teams": Team.objects.filter(all_players__first_name = "Samuel", all_players__last_name = "Evans"),
		# 10 todos los jugadores, pasados y presentes de los Gatos tigre de manitoba
		# "players": Player.objects.filter(all_teams__team_name = "Tiger-Cats", all_teams__location = "Manitoba")
		# 11 todos los jugadores que anteriormente estaban con los Wichita Vikings
		# "players": Player.objects.filter(all_teams__team_name = "Vikings", all_teams__location = "Wichita").exclude(curr_team__team_name = "Vikings", curr_team__location = "Wichita"),
		# 12 cada equipo para el que Jacob Gray jugo antes de unirse a los Oregon Colts
		#"teams": Team.objects.filter(all_players__first_name = "Jacob", all_players__last_name = "Gray").exclude(team_name = "Colts", location = "Oregon"),
		# 13 todos llamados Joshua que alguna vez han jugado en la Federacion Atlantica de Jugadores de Beisbol Amateur
		# "players": Player.objects.filter(first_name = "Joshua", all_teams__league__name = "Atlantic Federation of Amateur Baseball Players"),
		# 14 todos los equipos que han tenido 12 o mas jugadores, pasados y presente
		#"teams": Team.objects.annotate(x = Count('all_players')).filter(x__gt=11),
		# 15 todos los jugadores y el numero de equipos para los que jugo, ordenados por la cantidad de equipos para los que han jugado
		"players": Player.objects.annotate(x = Count('all_teams')).order_by('-x'),

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")