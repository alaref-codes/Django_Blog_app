from django.db import models
# This file whole purpose is to ensure that whenever a user is created  . . .
#  A new profile gets CREATED AND A NEW PROFILE GETS ASSIGNED THE USER USER

# This is why it called signals because it give a signal to the profile model or
# any model to get created automaticall

from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):   # minimizing the image size using the pillow package by overriding the save mothod

# by overriding the save method you can also delete old messages or something like that
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)



