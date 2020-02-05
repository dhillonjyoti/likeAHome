from django.db import models
from admin_app.models import UserRole


class PgDetails(models.Model):
    id= models.AutoField(primary_key=True)
    role_id= models.ForeignKey(UserRole, on_delete=models.CASCADE)
    pg_name = models.TextField(max_length=255, default="", null=True, blank=True)
    address = models.TextField(max_length=255, default="", null=True, blank=True)
    contact = models.BigIntegerField(default="", null=True, blank=True)
    address = models.TextField(max_length=255, default="", null=True, blank=True)
    images = models.TextField(max_length=255, default="", null=True, blank=True)
    location = models.TextField(max_length=255, default="", null=True, blank=True)
    description= models.TextField(max_length=255, default="", null=True, blank=True)

    def __str__(self):
        return self.pg_name