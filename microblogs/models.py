from django.core.validators import RegexValidator, MaxLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=30,unique=True,
                                validators=[RegexValidator(
                                    regex='^@[a-zA-Z0-9_-]{3,}$',
                                    message='username must consist of @ followed by at least three alphanumericals'
                                )])
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(blank=False,unique=True)
    bio = models.TextField(blank=True,validators=[MaxLengthValidator(520)])
