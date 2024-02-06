# Generated by Django 5.0.1 on 2024-01-23 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uid', models.CharField(max_length=20, unique=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.BooleanField(default=False)),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Faculty.faculty')),
            ],
        ),
    ]
