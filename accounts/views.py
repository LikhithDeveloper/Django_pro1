
from accounts.models import Profile
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_type = request.POST['user_type']  # Get user type from the form

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('/register/')
            else:
                user = User.objects.create_user(username=username, password=confirm_password, email=email, first_name=first_name, last_name=last_name)
                user.profile.user_type = user_type  # Set the user type
                user.save()
                messages.info(request, 'Successfully Registered')
                return redirect('/register/')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('/register/')
    else:
        return render(request, 'register.html')


