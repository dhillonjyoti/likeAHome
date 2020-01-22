from django import forms
from admin_app.models import RoleDetails


class RoleDetailsForm(forms.ModelForm):
    class Meta:
        model = RoleDetails
        exclude = ['id', 'role', 'first_name', 'last_name', 'email',
                   'password', 'mobile', 'address', 'gender', 'verify_link',
                   'otp', 'otp_time', 'is_active', 'image']
