from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.accounts import CustomerUser
from .models.profile import Profile


# Register your models here.

class CustomerUserAdmin(UserAdmin):
    model = CustomerUser

    list_display = ["email", "first_name", "is_active", "is_staff"]
    list_filter = ["is_active", "is_staff"]

    search_fields = ["email", "first_name", "last_name"]
    ordering = ["email"]

    # Add fields used in the add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2')}
         ),
    )

    # Fields for editing the user in the admin
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )


admin.site.register(CustomerUser, CustomerUserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "avatar", "bio", "birth_date", "region", "district", "address"]
    list_filter = ['region', 'district']
    search_fields = ["user__first_name"]


admin.site.register(Profile, ProfileAdmin)
