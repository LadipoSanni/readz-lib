from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='frontend_profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Book(models.Model):
    CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('technology', 'Technology'),
        ('science', 'Science'),
    ]

    PUBLISHER_CHOICES = [
        ('Wiley', 'Wiley'),
        ('Apress', 'Apress'),
        ('Manning', 'Manning'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=50, choices=PUBLISHER_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


from django.utils.timezone import now

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_on = models.DateTimeField(default=now)
    return_by = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
