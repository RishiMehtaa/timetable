# Generated by Django 5.2 on 2025-04-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_teaches_end_time_alter_teaches_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teaches',
            name='section',
            field=models.IntegerField(default=0),
        ),
    ]
