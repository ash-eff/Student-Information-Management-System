from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    district = models.ForeignKey("District", on_delete=models.CASCADE, blank=True, null=True)

class District(models.Model):
    pass