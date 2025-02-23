from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from frontend_api.models import Book, Borrow

class LibraryIntegrationTests(APITestCase):
    def setUp(self):
        self.user_data = {"username": "testuser", "email": "test@example.com"}
        self.book_data = {"title": "Integration Test Book", "author": "Test Author", "available": True}

    def test_user_borrows_book(self):
        """Full flow: Create user -> Add book -> Borrow book -> Check availability"""

        # Step 1: Create a user
        user_response = self.client.post(reverse("user-enroll"), self.user_data)
        self.assertEqual(user_response.status_code, status.HTTP_201_CREATED)
        user_id = user_response.data["id"]  # Get the new user's ID

        # Step 2: Add a book
        book = Book.objects.create(**self.book_data)
        self.assertTrue(book.available)  # Ensure the book is initially available

        # Step 3: Borrow the book
        borrow_url = reverse("borrow-book", args=[book.id])
        borrow_response = self.client.post(borrow_url, {"user_id": user_id, "days": 7})

        self.assertEqual(borrow_response.status_code, status.HTTP_201_CREATED)

        # Step 4: Check if the book is now unavailable
        book.refresh_from_db()
        self.assertFalse(book.available)

        print("Integration test passed! ✅")
