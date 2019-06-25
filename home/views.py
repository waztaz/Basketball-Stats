
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
from statistics import mode
from collections import Counter

def index(request):
    return render(request, 'home/home.html')

def statEvent(request):
    if request.method == 'POST':
        print("posting")
        body = json.loads(request.body.decode('utf-8'))
        event = body['event']
        player_id = body['current_player']
        quarter = body['quarter']
        print (quarter)
        player = Player.objects.get(player_id = player_id)
        print(event)
        if(event == 'make'):
            print("made basket")
            shot_value = body['shot_value']
            print("hello shot valueeeee" + str(shot_value))

            shot_location = body['court_location']
            bs = BasketballStat(event = event, 
                    player = player ,
                    shot_value = int(shot_value),
                    shot_location = int(shot_location),
                    quarter = int(quarter)
                    )
        elif(event == 'miss'):
            print("missed basket")
            shot_value = 0
            shot_location = body['court_location']
            print("TEST")
            print(player)
            bs = BasketballStat(event = event,
                    player = player,
                    shot_value = int(shot_value),
                    shot_location = int(shot_location),
                    quarter = int(quarter)
                    )
        else:
            bs = BasketballStat(event = event, player = player,quarter = int(quarter))
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

		

class analytics(generic.CreateView):
    def get(self,request,pk):
        current_coach = Coach.objects.get(user=self.request.user)
        queryset = Player.objects.filter(team_id=pk) 
        players = []
        ast = []
        hot = {}
        shots  = []
        shots3 = []
        quarter1 = []
        quarter2 = []
        quarter3 = []
        quarter4 = []
       
        for each in queryset:
            players.append(each)
            threes = (len(BasketballStat.objects.filter(player = each,shot_value = '3')))
            if threes == 0:
               threes = 1 
            ast.append(len(BasketballStat.objects.filter(player = each,event ='ast')))
            shots.append((len(BasketballStat.objects.filter(player = each,shot_value = '2')))/threes)
            quarter1.append(len(BasketballStat.objects.filter(player = each,quarter ='1')))
            quarter2.append(len(BasketballStat.objects.filter(player = each,quarter ='2')))
            quarter3.append(len(BasketballStat.objects.filter(player = each,quarter ='3')))
            quarter4.append(len(BasketballStat.objects.filter(player = each,quarter ='4')))
            print (BasketballStat.objects.filter(player = each,shot_value = '3'))
           
        

        #i = 0
        #for each in queryset:
        #    hot.append
        hot = []
        hot_send = []
        player_q = []
        for each in players:
            i = 0
            j = 0
            temp = []
            temp2 = []
            print("hello")
            for thing in (BasketballStat.objects.filter(player = each)):
                temp.append((BasketballStat.objects.filter(player = each)[i].shot_location))
                i = i +1
            l = [i for i in temp if i is not None]

            if len(l) == 0:
                hot.append(0)
            else:
                c = Counter(l)
                c = c.most_common(1)[0][0]
                print("most common" + str(c))
                hot.append(c)
            #temp2.append(l.flatten())   
            print ("hello" + str(hot))
            hotq = [quarter1[j],quarter2[j],quarter3[j],quarter4[j]]
            print (hotq)
            player_q.append(hotq.index(max(hotq))+1)
            j = j+1
            
        hot_map = {0:'not attempted shot', 1:'left corner three', 2:'left wing 3',4:'top left 3',5:'top right three', 6:' right corner three', 7:'right paint',8:'center paint',
        9:'left paint',10:'right mid range',11:'left mid range'}
        for each in hot:
            hot_send.append(hot_map[each])

        print (shots)
        print(player_q)

        total = zip(players,ast,hot_send,shots,player_q)
        return render(request, self.template_name,{'players':total,'coach':self.request.user,'ast':ast})

        



       
        


