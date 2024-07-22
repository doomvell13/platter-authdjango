from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Account(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_accounts')

    def __str__(self):
        return self.name

class HeadOffice(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def clean(self):
        existing_head_offices = HeadOffice.objects.filter(account=self.account)
        if self.pk:
            existing_head_offices = existing_head_offices.exclude(pk=self.pk)
        if existing_head_offices.exists():
            raise ValidationError("Cannot add new head office. There can only be one head office per account.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class DistrictOffice(models.Model):
    head_office = models.ForeignKey(HeadOffice, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BranchLocation(models.Model):
    district_office = models.ForeignKey(DistrictOffice, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.district_office.name})"
