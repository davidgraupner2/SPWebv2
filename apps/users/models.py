from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from apps.tenants.models import TenantAwareModel


class CustomUser(AbstractBaseUser, TenantAwareModel, PermissionsMixin):

    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=150, verbose_name='Last Name')
    email = models.EmailField(_('email address'), unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # Set the Username to email
    USERNAME_FIELD = 'email'

    # Set the required fields
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"