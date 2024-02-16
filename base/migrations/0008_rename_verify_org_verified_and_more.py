# Generated by Django 5.0.2 on 2024-02-16 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_registered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='org',
            old_name='verify',
            new_name='verified',
        ),
        migrations.AddField(
            model_name='events',
            name='Registration_option',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='events',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='Event_images/'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='vol_profile/'),
        ),
    ]