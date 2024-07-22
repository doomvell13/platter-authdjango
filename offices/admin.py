from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Account, HeadOffice, DistrictOffice, BranchLocation

@admin.register(HeadOffice)
class HeadOfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'account')
    search_fields = ('name', 'account__name')

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            form.add_error(None, str(e))

@admin.register(BranchLocation)
class BranchLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'district_office', 'get_head_office')
    list_filter = ('district_office', 'district_office__head_office')
    search_fields = ('name', 'district_office__name', 'district_office__head_office__name')

    def get_head_office(self, obj):
        return obj.district_office.head_office
    get_head_office.short_description = 'Head Office'
    get_head_office.admin_order_field = 'district_office__head_office'

@admin.register(DistrictOffice)
class DistrictOfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_office')
    list_filter = ('head_office',)
    search_fields = ('name', 'head_office__name')

admin.site.register(Account)
