from django import forms
from front_app.models import UserRole


class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        exclude = ['role_id', 'role_name']