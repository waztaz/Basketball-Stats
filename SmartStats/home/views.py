
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

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterFor

def index(request):
    return render(request, 'home/home.html')

class coachhome(LoginRequiredMixin,generic.CreateView):
    def get(self,request):
    	login_url = '/home/login/'
    	redirect_field_name = '/home/login'
    	players = ['Hello','Bye'] #This is where you put querries to database to select all players of the particular coach username of coahc can be provided by request.user
    	template_name = 'home/coachhome.html'
    	print (request.user)
    	return render(request, self.template_name,{'players':players})

		

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



