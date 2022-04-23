from django.db import models
from django.contrib.auth.models import AbstractUser


# Model for user
class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


# Lots available in the shelter
class Lot(models.Model):
    number = models.IntegerField()
    Yes = "Yes"
    No = "No"
    OCCUPIED_CHOICES = [
        (Yes, "Occupied"),
        (No, "Not Occupied")
    ]
    TYPE_CHOICES = [
        ("ST", "Short-term"),
        ("LT", "Long-term"),
        ("NIL", "")
    ]
    occupied_status = models.CharField(max_length=3, choices=OCCUPIED_CHOICES, default=No)
    type = models.CharField(max_length=4, choices=TYPE_CHOICES, default="NIL")

    def __str__(self):
        return f"{self.type}: Lot {self.number}"