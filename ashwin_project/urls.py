from django.contrib import admin
from django.urls import path, include # Add 'include' to the imports

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line tells Django to look for URLs inside the 'portfolio' app
    path('', include('firstapp.urls')), 
]