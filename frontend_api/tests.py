from django.contrib.auth.models import User
from django.urls import reverse  # 🔥 Use `reverse()` for dynamic URLs
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book, Borrow

class UserTests(APITestCase):
    def test_create_user(self):
        """Test user creation"""
        url = reverse("user-enroll")  # ✅ Use `reverse()` for consistency
        data = {"username": "testuser", "email": "test@example.com"}
        response = self.client.post(url, data)
        print("User Create Response:", response.status_code, response.json())  # Debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class BookTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="testuser", email="test@example.com")
        self.book = Book.objects.create(title="Test Book", author="Author", available=True)

    def test_borrow_book(self):
        url = reverse("borrow-book", args=[self.book.id])  # ✅ Use `reverse()`
        response = self.client.post(url, {"user_id": self.user.id, "days": 7})

        # Debugging output
        print("Borrow Book Response:", response.status_code, response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # ✅ Reload the book from the database
        self.book.refresh_from_db()
        self.assertFalse(self.book.available)  # ✅ Book should be unavailable

    def test_list_books(self):
        url = reverse("available-books")  # ✅ Use `reverse()`
        response = self.client.get(url)

        print("List Books Response:", response.status_code, response.json())  # Debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
