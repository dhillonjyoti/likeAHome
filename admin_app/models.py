from django.db import models


class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, default="", null=True, unique=True,
                                 blank=True)

    def __str__(self):
        return self.role_name


class RoleDetails(models.Model):
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default="", null=True, blank=True)
    last_name = models.CharField(max_length=255, default="", null=True, blank=True)
    email = models.EmailField(max_length=255, default="", blank=True, unique=True,
                              primary_key=True)
    password = models.CharField(max_length=255, default="", null=True, blank=True)
    mobile = models.BigIntegerField(default=0, null=True, blank=True)
    address = models.TextField(max_length=255, default="", null=True, blank=True)
    gender = models.CharField(max_length=255, default="", null=True, blank=True)
    verify_link = models.CharField(max_length=255, default="", null=True, blank=True)
    otp = models.CharField(max_length=255, default="", null=True, blank=True)
    otp_time = models.CharField(max_length=255, default="", null=True, blank=True)
    is_active = models.NullBooleanField(default=0)
    image = models.CharField(max_length=255, default="", null=True, blank=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
