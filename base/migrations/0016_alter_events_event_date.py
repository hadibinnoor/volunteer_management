# Generated by Django 5.0.2 on 2024-02-19 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_remove_events_event_disription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='Event_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
