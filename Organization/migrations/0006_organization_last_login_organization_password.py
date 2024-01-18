# Generated by Django 5.0.1 on 2024-01-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0005_remove_organization_area_organization_location_of'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='organization',
            name='password',
            field=models.CharField(default=123, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
