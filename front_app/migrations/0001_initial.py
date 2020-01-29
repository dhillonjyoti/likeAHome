# Generated by Django 2.0.6 on 2020-01-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(blank=True, default='', max_length=255, null=True, unique=True)),
            ],
        ),
    ]
