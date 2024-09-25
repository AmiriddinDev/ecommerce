"""
Create signals for the accounts app
"""

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models.accounts import CustomerUser
from .models.profile import Profile

@receiver(post_save, sender=CustomerUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
