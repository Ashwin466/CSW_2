from django.contrib import admin
from django.urls import path
from firstapp.views import *  # Import the views.py file we made in Step 2

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path('admin/',admin.site.urls),
    path('blog/',blog,name="blog"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()
