# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('BrainTech_App.urls')),  # This includes your app's URLs
# ]
# BrainTech_technology/urls.py

from django.contrib import admin
from django.urls import path, include  # Add 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BrainTech_App.urls')),  # Include the app-level urls.py
]
