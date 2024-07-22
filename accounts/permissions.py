from django.contrib.auth.decorators import user_passes_test

def is_head_office_user(user):
    return user.userprofile.access_level == 'HO'

def is_district_office_user(user):
    return user.userprofile.access_level == 'DO'

def is_branch_location_user(user):
    return user.userprofile.access_level == 'BL'

def head_office_required(view_func):
    decorated_view_func = user_passes_test(is_head_office_user, login_url='dashboard')(view_func)
    return decorated_view_func

def district_office_required(view_func):
    decorated_view_func = user_passes_test(is_district_office_user, login_url='dashboard')(view_func)
    return decorated_view_func

def branch_location_required(view_func):
    decorated_view_func = user_passes_test(is_branch_location_user, login_url='dashboard')(view_func)
    return decorated_view_func