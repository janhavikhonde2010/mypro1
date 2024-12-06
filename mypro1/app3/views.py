from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Registration

def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        name = request.POST['name']
        email_id = request.POST['email_id']
        mobile_no = request.POST['mobile_no']
        password = request.POST['password']

        # Check if email already exists
        if Registration.objects.filter(email_id=email_id).exists():
            messages.error(request, 'Email ID already exists.')
            return redirect('app3:register')  # Redirect to registration page if email exists

        # Create a new Registration instance and save
        registration = Registration(username=username, name=name, email_id=email_id, mobile_no=mobile_no, password=password)
        registration.save()

        # Display a success message
        messages.success(request, 'Registration successful! You can now log in.')

        # Redirect to login page after successful registration
        return redirect('app2:signup')
        # Adjust 'app3:login' to the actual name of your login URL in app3

    return render(request, 'register.html')
def home(request):
    return render(request, 'a.html')