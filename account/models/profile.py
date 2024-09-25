from django.db import models

from .accounts import CustomerUser
from common.models import BaseModel, Region, District
from common.file_path_renamer import PathAndRenamer

user_avatar_path = PathAndRenamer('avatars/')

class Profile(BaseModel):
    user = models.OneToOneField(CustomerUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_avatar_path, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} Profile"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'