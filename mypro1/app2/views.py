from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            # If user exists, attempt login
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # If authentication is successful
                login(request, user)
                messages.success(request, "Login successful!")
                return render(request, 'b.html')  # Render b.html directly
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Username does not exist.")

    return render(request, 'signup.html')
