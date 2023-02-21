from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ClientUserCreationForm, ClientUserChangeForm
from .models import ClientUser

# Register your models here.


class ClientUserAdmin(UserAdmin):
    add_form = ClientUserCreationForm
    form = ClientUserChangeForm
    model = ClientUser
    list_display = [
        'email',
        'username',
        'name',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)


admin.site.register(ClientUser, ClientUserAdmin)
