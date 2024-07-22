from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.conf import settings
from django.utils.translation import gettext_lazy as _  # Add this import

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
    email = models.EmailField(_('email address'), unique=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='custom_users'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.pk:
            # If the user already exists, remove all groups
            self.groups.clear()
        super().save(*args, **kwargs)
        if self.group:
            # Add the user to the selected group
            self.groups.add(self.group)

class UserProfile(models.Model):
    ACCESS_LEVELS = (
        ('HO', 'Head Office'),
        ('DO', 'District Office'),
        ('BL', 'Branch Location'),
    )
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account = models.ForeignKey('offices.Account', on_delete=models.CASCADE)
    access_level = models.CharField(max_length=2, choices=ACCESS_LEVELS)
    district_office = models.ForeignKey('offices.DistrictOffice', on_delete=models.SET_NULL, null=True, blank=True)
    branch_location = models.ForeignKey('offices.BranchLocation', on_delete=models.SET_NULL, null=True, blank=True)