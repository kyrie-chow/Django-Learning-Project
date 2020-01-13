from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_user')
    birthday = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "profile for {}".format(self.user.username)
