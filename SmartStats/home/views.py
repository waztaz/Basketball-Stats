
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm
import sys
from django.db.models import Avg, Count
sys.path.append("..")
from roster.models import User, Coach, Team, Player, BasketballStat

def index(request):
    return render(request, 'home/home.html')

def statEvent(request):
    if request.method == 'POST':
        print("posting")
        body = json.loads(request.body.decode('utf-8'))
        print(body)
        event = body['event']
        player_id = body['current_player']
        print(player_id)
        player = Player.objects.get(player_id = player_id)
        print(event)
        if(event == 'make'):
            print("made basket")
            shot_value = body['shot_value']
            shot_location = body['court_location']
            bs = BasketballStat(event = event, 
                    player = int(player), 
                    shot_value = int(shot_value),
                    shot_location = int(shot_location)
                    )
        elif(event == 'miss'):
            print("missed basket")
            shot_value = 0
            shot_location = body['court_location']
            print(shot_location)
            bs = BasketballStat(event = event,
                    player = int(player),
                    shot_value = int(shot_value),
                    shot_location = int(shot_location)
                    )
        else:
            bs = BasketballStat(event = event, player = player)
        print(bs.event)
        bs.save()
        return HttpResponse("Success")
        

    return HttpResponse("Not a POST")

class coachhome(generic.CreateView):
    player_stats = dict()
    lineups =[]

    def get(self,request,pk):
        current_coach = Coach.objects.get(user=self.request.user)
        queryset = Player.objects.filter(team=pk)
        players = []
        for each in queryset:
            players.append(each)

            coachhome.player_stats.update({str(each) : [0,0,0,0,0,0]} )
            print (coachhome.player_stats['kk'])


            #player_stats['player'] == eac

        if str(self.request.user) != "AnonymousUser":
    	       #players = ['Hello','Bye',"Test1","Test2","Test3","Test4"] 
    	       template_name = 'home/coachhome.html'
    	       print ("hello" + str(self.request.user))
    	       return render(request, self.template_name,{'players':players,'coach':self.request.user})
        else:
               return redirect('/accounts/login')


    def post(self,request):

        

        body = json.loads(request.body.decode('utf-8'))
        
        if body['selector'] == 'stat':
            print(body)
            current_player
            body['current_player']
        if body['selector'] == 'shot':
            print (body)
        if body['selector'] == 'subs':
            print(body)
        return HttpResponse(200)

		

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home/coachhome')
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})



