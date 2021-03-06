# Generated by Django 2.0.6 on 2020-01-22 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoleDetails',
            fields=[
                ('first_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=255, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('mobile', models.BigIntegerField(blank=True, default=0, null=True)),
                ('address', models.TextField(blank=True, default='', max_length=255, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('verify_link', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('otp', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('otp_time', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('is_active', models.NullBooleanField()),
                ('image', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(blank=True, default='', max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='roledetails',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.UserRole'),
        ),
    ]
