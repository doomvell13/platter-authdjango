from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import DistrictOffice, BranchLocation
from .forms import DistrictOfficeForm, BranchLocationForm

def is_head_office_user(user):
    return user.userprofile.access_level == 'HO'

def is_district_office_user(user):
    return user.userprofile.access_level == 'DO'

@login_required
@user_passes_test(is_head_office_user)
def create_district_office(request):
    if request.method == 'POST':
        form = DistrictOfficeForm(request.POST)
        if form.is_valid():
            district_office = form.save(commit=False)
            district_office.head_office = request.user.userprofile.account.headoffice
            district_office.save()
            return redirect('dashboard')
    else:
        form = DistrictOfficeForm()
    return render(request, 'offices/create_district_office.html', {'form': form})

@login_required
@user_passes_test(is_district_office_user)
def create_branch_location(request):
    if request.method == 'POST':
        form = BranchLocationForm(request.POST)
        if form.is_valid():
            branch_location = form.save(commit=False)
            branch_location.district_office = request.user.userprofile.district_office
            branch_location.save()
            return redirect('dashboard')
    else:
        form = BranchLocationForm()
    return render(request, 'offices/create_branch_location.html', {'form': form})