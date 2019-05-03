from django.urls import path
#from account.forms import LoginForm
from django.views.generic.base import TemplateView # new


from . import views

app_name = 'home'

urlpatterns = [
        #ex: /roster/
        path('', views.index, name='index'),
        path('coachhome/<int:pk>', views.coachhome.as_view(template_name='coachhome.html'), name='coachhome'),
        path('coachhome/1',views.coachhome.as_view(template_name='coachhome.html')),
        path('coachhome/2',views.coachhome.as_view(template_name='coachhome.html')),
        path('coachhome/3',views.coachhome.as_view(template_name='coachhome.html')), # ne
        path('coachhome/subs',views.coachhome.as_view(template_name='coachhome.html')),
        path('coachhome/shot',views.coachhome.as_view(template_name = 'coachhome.html')), 
        path('coachhome/stat',views.coachhome.as_view(template_name='coachhome.html')),
        path('coachhome/event', views.statEvent, name='statEvent'),
        path('coachhome/analytics/<int:pk>', views.analytics.as_view(template_name= 'analytics.html'), name='analytics'),



]
