from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

# offices/models.py

from django.db import models
from django.conf import settings

class Account(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_accounts')

class HeadOffice(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class DistrictOffice(models.Model):
    head_office = models.ForeignKey(HeadOffice, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class BranchLocation(models.Model):
    district_office = models.ForeignKey(DistrictOffice, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class UserProfile(models.Model):
    ACCESS_LEVELS = (
        ('HO', 'Head Office'),
        ('DO', 'District Office'),
        ('BL', 'Branch Location'),
    )
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=2, choices=ACCESS_LEVELS)
    district_office = models.ForeignKey(DistrictOffice, on_delete=models.SET_NULL, null=True, blank=True)
    branch_location = models.ForeignKey(BranchLocation, on_delete=models.SET_NULL, null=True, blank=True)