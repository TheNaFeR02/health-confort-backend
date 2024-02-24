from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.models import EmailAddress

# Create your models here.
class User(AbstractUser):
  role = models.CharField(max_length=100, default='basic')

  def delete(self, *args, **kwargs):
        EmailAddress.objects.filter(user=self).delete() # remove the email when user is deleted
        super().delete(*args, **kwargs)
  
  def __str__(self):
    return self.username


  