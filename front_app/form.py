from django import forms
from front_app.models import UserRole,RoleDetails


class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        exclude = ['role_id', 'role_name']


class RoleDetailsForm(forms.ModelForm):
    class Meta:
        model = RoleDetails
        exclude = ['name','email','password','address','gender','verify_link','otp','otp_time','is_active']