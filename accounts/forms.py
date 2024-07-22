from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile
from offices.models import Account, DistrictOffice, BranchLocation

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('access_level', 'district_office', 'branch_location')

    def __init__(self, *args, **kwargs):
        account = kwargs.pop('account', None)
        super().__init__(*args, **kwargs)
        if account:
            self.fields['district_office'].queryset = DistrictOffice.objects.filter(head_office__account=account)
            self.fields['branch_location'].queryset = BranchLocation.objects.filter(district_office__head_office__account=account)