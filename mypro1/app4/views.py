# app4/views.py
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')  # Renders home.html from the global templates folder
