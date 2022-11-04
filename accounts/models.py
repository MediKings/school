from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    objects = UserManager()

    def __str__(self):
        return f'{self.username}'


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(default='picture/default_profile.png', upload_to='picture/', null=True, blank=True)
    ville = models.CharField(max_length=30, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'
