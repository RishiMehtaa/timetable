# Generated by Django 5.0.4 on 2025-04-12 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.IntegerField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=255)),
                ('branch_abr', models.CharField(max_length=10)),
                ('branch_floor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=255)),
                ('room_type', models.CharField(max_length=50)),
                ('room_floor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=255)),
                ('subject_abr', models.CharField(max_length=10)),
                ('subject_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('t_staff_floor', models.IntegerField()),
                ('t_staff_room', models.IntegerField()),
                ('t_staff_layout', models.ImageField(upload_to='staffroom_layouts/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sap_id', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_no', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('class_id', models.CharField(max_length=2)),
                ('section', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('AY', models.DateField()),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.branch')),
            ],
        ),
        migrations.CreateModel(
            name='BranchSub',
            fields=[
                ('bs_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sem', models.IntegerField()),
                ('scheme', models.CharField(max_length=50)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.branch')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField()),
                ('class_id', models.CharField(max_length=2)),
                ('section', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('day', models.CharField(max_length=20)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.room')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.teacher')),
            ],
        ),
    ]
