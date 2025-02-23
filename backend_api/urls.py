from django.urls import path
from .views import (
    AdminBookListCreateView, AdminBookDetailView,
    AdminProfileListCreateView, AdminProfileDetailView
)

urlpatterns = [
    # 📚 Book management URLs
    path('books/', AdminBookListCreateView.as_view(), name='admin-book-list'),
    path('books/<int:pk>/', AdminBookDetailView.as_view(), name='admin-book-detail'),

    # 👤 Profile management URLs
    path('profiles/', AdminProfileListCreateView.as_view(), name='admin-profile-list'),
    path('profiles/<int:pk>/', AdminProfileDetailView.as_view(), name='admin-profile-detail'),
]
