from django import forms
from .models import DistrictOffice, BranchLocation

class DistrictOfficeForm(forms.ModelForm):
    class Meta:
        model = DistrictOffice
        fields = ['name']

class BranchLocationForm(forms.ModelForm):
    class Meta:
        model = BranchLocation
        fields = ['name']