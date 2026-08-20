from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email =  models.EmailField('email address',  unique=True)
    
    def __str__(self)  -> str:
        return self.email or self.username