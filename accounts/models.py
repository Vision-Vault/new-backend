from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    profile_picture = CloudinaryField('ProfileImage',overwrite= True,format="jpg",null= True)
    bio = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
