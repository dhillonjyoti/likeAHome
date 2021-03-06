# Generated by Django 2.0.6 on 2020-01-09 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleDetails',
            fields=[
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=255, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('mobile', models.BigIntegerField(blank=True, default='', null=True)),
                ('address', models.TextField(blank=True, default='', max_length=255, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('verify_link', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('otp', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('otp_time', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('is_active', models.NullBooleanField(default=0)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_app.UserRole')),
            ],
        ),
    ]
