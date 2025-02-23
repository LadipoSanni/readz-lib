from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book

class AdminBookTests(TestCase):
    databases = {"default", "backend"}  # Explicitly allow both databases

    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="adminpass")
        self.book = Book.objects.create(title="Admin Book", author="Admin Author", available=True)

    def test_admin_can_create_book(self):
        """Test if admin can create books"""
        book = Book.objects.create(title="New Book", author="New Author", available=True)
        self.assertEqual(Book.objects.count(), 2)
