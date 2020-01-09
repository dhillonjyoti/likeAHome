from django.db import models

class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, default="", null=True ,unique=True, blank=True)

class RoleDetails(models.Model):
    role_id = models.ForeignKey(UserRole,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="" ,null=True, blank=True)
    email = models.EmailField(max_length=255, default="", blank=True, unique=True, primary_key=True)
    password = models.CharField(max_length=255, default="", null=True, blank=True)
    mobile = models.BigIntegerField(default="", null=True, blank=True)
    address = models.TextField(max_length=255, default="", null=True, blank=True)
    gender = models.CharField(max_length=255, default="", null=True, blank=True)
    verify_link = models.CharField(max_length=255, default="", null=True, blank=True)
    otp = models.CharField(max_length=255, default="", null=True, blank=True)
    otp_time = models.CharField(max_length=255, default="", null=True, blank=True)
    is_active = models.NullBooleanField(default=0)