from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count



from . import team_maker

def index(request):
	context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
		# "leagues": League.objects.filter(sport__contains='baseball')
		# "leagues": League.objects.filter(name__contains='womens')
		# "leagues": League.objects.filter(sport__contains='hockey')
		# "leagues": League.objects.exclude(sport__contains='football')
		# "leagues": League.objects.filter(name__contains='conference')
		# "leagues": League.objects.filter(name__contains='atlantic')
		# "teams": Team.objects.filter(location__contains='dallas')
		# "teams": Team.objects.filter(team_name__contains='raptor')
		# "teams": Team.objects.filter(location__contains='city')
		# "teams": Team.objects.filter(team_name__startswith='T')
		# "teams": Team.objects.order_by("location")
		# "teams": Team.objects.order_by('-team_name')
		# "players": Player.objects.filter(last_name__contains="cooper")
		# "players": Player.objects.filter(first_name__contains="joshua")
		# "players": Player.objects.filter(last_name__contains="cooper").exclude(first_name__contains="joshua")
		# "players": Player.objects.filter(Q(first_name__contains = 'Wyatt') | Q(first_name__contains = 'Alexander'))
		# "teams" : Team.objects.filter(league__name__contains="Atlantic Soccer Conference")
		# "players": Player.objects.filter(curr_team__team_name__contains="penguins")
		# "players": Player.objects.filter(curr_team__league__name__contains="collegiate baseball")
		# "players": Player.objects.filter(Q(curr_team__league__name__contains="amateur football") & Q(last_name__contains='Lopez'))
		# "players": Player.objects.filter(curr_team__league__sport__contains="football")
		# "teams": Team.objects.filter(curr_players__first_name__contains="sophia")
		# "leagues": League.objects.filter(teams__curr_players__first_name__contains="sophia")
		# "players": Player.objects.filter(last_name__contains="flores").exclude(curr_team__team_name__contains="roughriders")
		# "teams": Team.objects.filter(Q(all_players__first_name__contains='samuel') & Q(all_players__last_name__contains='evans'))
		# "players": Player.objects.filter(all_teams__team_name__contains='tiger')
		# "players": Player.objects.filter(all_teams__team_name__contains='vikings').exclude(curr_team__team_name__contains='vikings')
		# "teams" : Team.objects.all().annotate(player_count=Count('all_players')).filter(player_count__gte=12)
		"players" : Player.objects.all().annotate(team_count=Count('all_teams')).order_by('-team_count')
	}

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

	/courses/destroy/{{Courses.id}}