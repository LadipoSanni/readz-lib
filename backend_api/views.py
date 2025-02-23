from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Book, Profile
from .serializers import BookSerializer, ProfileSerializer

# ✅ Admin can add, list, update, and delete books
class AdminBookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AdminBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ✅ Admin can manage user profiles
class AdminProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class AdminProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
