from datetime import timedelta
from django.utils.timezone import now
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Borrow
from .serializers import UserSerializer, BookSerializer, BorrowSerializer


# 1. Enroll users (Allows listing users too)
class UserCreateView(generics.ListCreateAPIView):  # Supports both listing and creating users
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 2. List all available books
class AvailableBooksView(generics.ListAPIView):
    queryset = Book.objects.filter(available=True)
    serializer_class = BookSerializer


# 3. Get a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# 4. Filter books by publisher and category
class FilterBooksView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(available=True)
        publisher = self.request.query_params.get('publisher', '').strip()
        category = self.request.query_params.get('category', '').strip()

        if publisher:
            queryset = queryset.filter(publisher__iexact=publisher)  # Case-insensitive filtering
        if category:
            queryset = queryset.filter(category__iexact=category)  # Case-insensitive filtering

        return queryset


# 5. Borrow books (Mark book as unavailable)
class BorrowBookView(APIView):
    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id, available=True)
            user = User.objects.get(id=request.data.get('user_id'))

            # Check if user has already borrowed the book
            if Borrow.objects.filter(user=user, book=book).exists():
                return Response({"error": "User already borrowed this book"}, status=status.HTTP_400_BAD_REQUEST)

            # Ensure `days` is a valid number
            try:
                days = int(request.data.get('days', 7))
                if days <= 0:
                    raise ValueError("Days must be positive")
            except ValueError:
                return Response({"error": "Invalid number of days"}, status=status.HTTP_400_BAD_REQUEST)

            borrow = Borrow.objects.create(
                user=user, book=book, return_by=now() + timedelta(days=days)
            )
            book.available = False  # Mark book as unavailable
            book.save()

            return Response(BorrowSerializer(borrow).data, status=status.HTTP_201_CREATED)
        except Book.DoesNotExist:
            return Response({"error": "Book not available"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

        
class ReturnBookView(APIView):
    def post(self, request, book_id):
        try:
            # Check if the book exists and has been borrowed
            borrow = Borrow.objects.get(book_id=book_id, returned=False)
            book = borrow.book  # Get the related book

            # Mark book as available again
            book.available = True
            book.save()

            # Update borrow record
            borrow.returned = True
            borrow.save()

            return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)
        except Borrow.DoesNotExist:
            return Response({"error": "This book is not currently borrowed or has already been returned"},
                            status=status.HTTP_400_BAD_REQUEST)
