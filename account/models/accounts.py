from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from ..managers import CustomUserManager

class CustomerUser(AbstractUser, PermissionsMixin):
    """
    Custom user model
    """
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'customer_user'
