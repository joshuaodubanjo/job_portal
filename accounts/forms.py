from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ClientUser


class ClientUserCreationForm(UserCreationForm):
    class Meta:
        model = ClientUser
        fields = UserCreationForm.Meta.fields + ("name",)


class ClientUserChangeForm(UserChangeForm):
    class Meta:
        model = ClientUser
        fields = UserChangeForm.Meta.fields