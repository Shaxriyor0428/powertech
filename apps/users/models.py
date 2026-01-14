from django.contrib.auth.models import AbstractUser
from django.db import models
from common.base_model import BaseModel

class User(AbstractUser, BaseModel):
    username =  models.CharField( max_length=150, unique=True )
    password = models.CharField(null=True, blank=True)
    full_name = models.CharField(blank=True, null=True, max_length=250)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username or f"User {self.id}"
