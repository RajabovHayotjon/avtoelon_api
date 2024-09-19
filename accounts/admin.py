from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import AuthCode, User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("phone_number", "is_staff", "is_active",)
    list_filter = ("phone_number", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "phone_number", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("phone_number",)
    ordering = ("phone_number",)


admin.site.register(User, UserAdmin)
admin.site.register(AuthCode)