from django.urls import path, include
from django.contrib import admin
from django.urls import path
from .views import home  # Ensure this view exists
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_api.urls')),  # Include API URLs correctly
    path('', home, name='user-api-home'),
]
