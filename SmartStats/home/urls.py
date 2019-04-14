from django.urls import path
#from account.forms import LoginForm
from django.views.generic.base import TemplateView # new


from . import views

urlpatterns = [
        #ex: /roster/
        path('', views.index, name='index'),
        path('signup/', views.signup, name='signup'),
        path('coachhome', views.coachhome.as_view(template_name='coachhome.html'), name='coachhome'), # new


]