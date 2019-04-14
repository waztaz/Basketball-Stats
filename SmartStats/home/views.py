
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

#from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, 'home/home.html')



class coachhome(generic.CreateView):
    def get(self,request):
    	template_name = 'home/coachhome.html'
    	return render(request, self.template_name)

