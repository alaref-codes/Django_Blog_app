from django.db.models.signals import post_save # this is the acutal signal
from django.contrib.auth.models import User
from django.dispatch import receiver # is a function that get the signal and do something with it
from .models import Profile


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance) # if a user is created then create a profile to that user

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save() # if a user is saved then saved a profile to that user


# then imoprt the signal to the app.py file  in a ready function
