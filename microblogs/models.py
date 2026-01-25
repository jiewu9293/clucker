from django.core.validators import RegexValidator, MaxLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from libgravatar import Gravatar
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
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def gravatar(self, size=120):
        """Return a URL to the user's gravatar."""
        gravatar_object = Gravatar(self.email)
        gravatar_url = gravatar_object.get_image(size=size, default='mp')
        return gravatar_url

    def mini_gravatar(self):
        """Return a URL to a miniature version of the user's gravatar."""
        return self.gravatar(size=60)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']