# Generated by Django 5.0 on 2024-02-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_events_event_disription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]