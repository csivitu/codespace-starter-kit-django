from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from app.forms import SignUpForm

#Forms demo
def signup(request):
    #Check if the user is submitting the sign-up form
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            #Create a user object and save it
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'])
            user.save()
            return HttpResponseRedirect('/app')

    #If the sign up page is requested,serve that
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

#Login_required decorator is to tell the django auth that the view requires login
@login_required(login_url='auth/login')
def logindemo(request):

    msg = "You are authorized"
    return HttpResponse(msg)


#You can create view functions here,define the logic and then map these views in url.py file
#If you need a view to be accessed by only logged-in users add the inbuilt decorator '@login_required'
