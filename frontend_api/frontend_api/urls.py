from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('frontend_api.urls')),  # 👌 Avoids recursion issues
]