from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser)
    ROLE_CHOICES = [
        ('admin','admin'),
        ('technicien', 'technicien'),
        ('Superviseur', 'Superviseur'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

