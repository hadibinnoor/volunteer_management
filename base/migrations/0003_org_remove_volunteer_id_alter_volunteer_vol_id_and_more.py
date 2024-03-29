# Generated by Django 5.0.1 on 2024-01-25 03:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_volunteer_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Org_ID', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('Org_Name', models.CharField(max_length=20)),
                ('Location', models.CharField(max_length=50)),
                ('verify', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='id',
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='Vol_ID',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('Event_ID', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('Number_of_Volunteer', models.PositiveIntegerField(verbose_name='Number of Volunteers')),
                ('Size_of_Event', models.PositiveIntegerField(verbose_name='Size of Event')),
                ('Event_Name', models.CharField(max_length=20, verbose_name='Event Name')),
                ('Location', models.CharField(max_length=20, verbose_name='Location')),
                ('Event_Date', models.DateTimeField(null=True)),
                ('Event_Status', models.CharField(choices=[('PAST', 'Past'), ('COMING', 'Coming')], default='COMING', max_length=20)),
                ('Created_Org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conducting_Org', to='base.org')),
            ],
        ),
        migrations.CreateModel(
            name='Reg_Volunteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Register', models.BooleanField(default=False)),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.events', verbose_name='Record_Event')),
                ('Volunteer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.volunteer', verbose_name='Record_Volunteer')),
            ],
        ),
    ]
