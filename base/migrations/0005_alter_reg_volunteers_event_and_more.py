# Generated by Django 5.0.2 on 2024-02-11 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_user_remove_org_is_active_remove_org_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_volunteers',
            name='Event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='base.events'),
        ),
        migrations.AlterField(
            model_name='reg_volunteers',
            name='Volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Record_Volunteer', to='base.volunteer'),
        ),
    ]
