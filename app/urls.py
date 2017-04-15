from django.conf.urls import url
from app.views import *
from django.contrib.auth.views import login
from app.forms import LoginForm

#The patterns (regex) below map url to view functions

urlpatterns = [
	
    url('auth/signup$',signup,name='signup'),
    url('app$',logindemo),
    #For login we have used an inbuilt form with custom template 'login.html'
    url('auth/login$',login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login')
]


