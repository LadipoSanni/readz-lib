from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Book, Borrow

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Using ID reference instead

    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields

class BorrowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Allowing user selection
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())  # Allowing book selection

    class Meta:
        model = Borrow
        fields = ['user', 'book', 'borrowed_on', 'return_by']
