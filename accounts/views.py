from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile
from offices.models import Account, HeadOffice, DistrictOffice, BranchLocation

@login_required
def dashboard(request):
    user_profile = request.user.userprofile
    context = {
        'user_profile': user_profile,
    }
    
    if user_profile.access_level == 'HO':
        context['district_offices'] = DistrictOffice.objects.filter(head_office__account=user_profile.account)
    elif user_profile.access_level == 'DO':
        context['branch_locations'] = BranchLocation.objects.filter(district_office=user_profile.district_office)
    
    return render(request, 'accounts/dashboard.html', context)

def is_account_owner(user):
    return user.userprofile.access_level == 'HO' and user.owned_accounts.exists()

@user_passes_test(is_account_owner)
@login_required
def create_user(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST, account=request.user.userprofile.account)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.account = request.user.userprofile.account
            profile.save()
            messages.success(request, 'User created successfully.')
            return redirect('user_list')
        else:
            messages.error(request, 'There was an error creating the user. Please check the form and try again.')
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserProfileForm(account=request.user.userprofile.account)
    return render(request, 'accounts/create_user.html', {'user_form': user_form, 'profile_form': profile_form})

@user_passes_test(is_account_owner)
@login_required
def user_list(request):
    users = UserProfile.objects.filter(account=request.user.userprofile.account)
    return render(request, 'accounts/user_list.html', {'users': users})

@user_passes_test(is_account_owner)
@login_required
def edit_user(request, user_id):
    user_profile = UserProfile.objects.get(id=user_id, account=request.user.userprofile.account)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile, account=request.user.userprofile.account)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserProfileForm(instance=user_profile, account=request.user.userprofile.account)
    return render(request, 'accounts/edit_user.html', {'form': form, 'user_profile': user_profile})