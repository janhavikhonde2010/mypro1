"""
URL configuration for mypro1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project/urls.py
# app4/views.py
# app4/urls.py
# app4/urls.py

# app4/urls.py
from django.urls import path
from app4 import views

urlpatterns = [
    path('about/', views.about, name='about'),  # This will be the URL for the home page
]
# Assuming home.html is in the global templates folder



