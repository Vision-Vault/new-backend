from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _



def upload_to(instance, filename):
    return 'accounts/{filename}'.format(filename=filename)

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(_("Image"), upload_to=upload_to, default='accounts/default.jpg')
    bio = models.TextField(default='add your BIO here',null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
