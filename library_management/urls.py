"""
URL configuration for library_management project.

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
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({"message": "Welcome to the Library Management API!"})

urlpatterns = [
    path('', home),  # New homepage route
    path('admin/', admin.site.urls),
    path('api/frontend/', include('frontend_api.urls')),
    path('admin/', admin.site.urls),  # Django Admin panel
    path('api/frontend/', include('frontend_api.urls')),  # Frontend API routes
    path('api/backend/', include('backend_api.urls')),  # Backend (Admin) API routes

]




