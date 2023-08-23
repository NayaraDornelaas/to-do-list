"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

############# MY COMMENTS ###########################
# If you have a view function in your views.py, connect it to a URL inside the urls.py to allow request routing
""" When a client requests a page by accessing a URL, Django matches the URL pattern by iterating through the list of all the URLs in your project URL configuration.
If Django matches that particular URL pattern, Django uses the view connected to the URL endpoint.
The view processes the information and returns an HTTP object to the user. Mainly, the HTTP object includes an HTML page of the URL endpoint requested.
*Source: https://ngangasn.com/what-are-views-and-urls-in-django-explained-in-simple-terms/#google_vignette"""



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls'))
]
