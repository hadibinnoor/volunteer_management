# Generated by Django 5.0.1 on 2024-01-18 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_alter_events_created_org_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='Volunteers',
        ),
    ]