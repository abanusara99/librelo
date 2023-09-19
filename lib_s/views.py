

from django.shortcuts import render, redirect
from .models import Registration, Log
from django.contrib.auth import authenticate, login as auth_login

def welcome(request):

    return render(request, 'welcome.html')

def register(request):
    if request.method == 'POST':
        # Get data from the POST request
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        accredat = request.POST['accredat']
        date = request.POST['dob']

        # Create a new Registration object and save it to the database
        regi = Registration(
            name=name,
            username=username,
            password=password,
            accredat=accredat,
            date=date
        )
        regi.save()

        # Save the username and password to the logdb table
        log = Log(
            username=username,
            password=password
        )
        log.save()

        return redirect('login') 
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        # Get data from the POST request
        username = request.POST['username']
        password = request.POST['password']

        # Check if the user exists in the regdb table
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If the user exists, log them in
            auth_login(request, user)
        else:
            # User authentication failed
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')