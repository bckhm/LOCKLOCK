from django.db import models
from django.contrib.auth.models import AbstractUser


# Model for user
class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


# Lots available in the shelter
class Lot(models.Model):
    number = models.IntegerField(max_length=2)
    Yes = "Yes"
    No = "No"
    OCCUPIED_CHOICES = [
        (Yes, "Occupied"),
        (No, "Not Occupied")
    ]
    occupied_status = models.CharField(max_length=3, choices=OCCUPIED_CHOICES, default=None)

# Registered Bicycles
class Bike(models.Model):
    # Maybe add an image model
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bike', default=None)
    current_lot = models.OneToOneField(Lot, on_delete=models.DO_NOTHING, related_name='bike', default=None)
