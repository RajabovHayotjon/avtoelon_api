from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    """Custom user model that supports using phone_number instead of username"""

    phone_number = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    telegram_id = models.CharField(
        max_length=30, unique=True, blank=True, null=True)

    USERNAME_FIELD = 'phone_number'

    def save(self, *args, **kwargs):
        self.phone_number = self.phone_number.replace(" ", "")
        self.phone_number = self.phone_number.replace("+", "")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number

    objects = UserManager()


class AuthCode(models.Model):
    code = models.CharField(max_length=6)
    user = models.ForeignKey(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    sent_to_adress = models.EmailField(max_length=200)

    def __str__(self):
        return self.code