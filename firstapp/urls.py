from django.contrib import admin
from django.urls import path
from firstapp.views import *  # Import the views.py file we made in Step 2

urlpatterns = [
    # '' means the home page (http://127.0.0.1:8000/)
    # views.home calls the function we defined in views.py
    path('',home, name='home'),
    path('delete/<id>/',delete,name="delete"),
    path('update/<id>/',update,name="update"),
    path('login1/',login1),
    path('signup1/',signup1),
    path('homeafter/',homeafter),
    path('logout1/',logout1,name="logoutpage"),
    path('admin/',admin.site.urls)
   

]
