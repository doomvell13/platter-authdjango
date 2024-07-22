from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'group')
    list_filter = ('is_staff', 'is_active', 'group')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'group', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'group'),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        fieldsets = list(super().get_fieldsets(request, obj))
        if obj.is_superuser:
            fieldsets[2][1]['fields'] = ('is_active', 'is_staff', 'is_superuser', 'group', 'user_permissions')
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.is_superuser:
            return ['is_superuser', 'email'] + list(self.readonly_fields)
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if change and 'is_superuser' in form.changed_data:
            # Prevent changing superuser status
            raise ValidationError("Superuser status cannot be changed.")
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(is_superuser=False)
        return qs

admin.site.register(CustomUser, CustomUserAdmin)