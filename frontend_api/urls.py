from .views import BorrowBookView, ReturnBookView
from django.contrib import admin
from user_api.views import home
from django.urls import path, include

from .views import (
    UserCreateView, AvailableBooksView, BookDetailView, FilterBooksView, BorrowBookView
)

urlpatterns = [
    path('api/users/', UserCreateView.as_view(), name='user-enroll'),
    path('api/books/', AvailableBooksView.as_view(), name='available-books'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/books/filter/', FilterBooksView.as_view(), name='filter-books'),
    path('api/books/<int:book_id>/borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('api/borrow/<int:book_id>/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:book_id>/', ReturnBookView.as_view(), name='return-book'),
    path('admin/', admin.site.urls),
    path('api/', home),  # Example API route
    path('api/', include('user_api.urls')),
    path('api/', include('user_api.urls')),  # Include your API routes

]




