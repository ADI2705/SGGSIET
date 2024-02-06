# Generated by Django 5.0.1 on 2024-01-23 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Faculty', '0001_initial'),
        ('department', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_paid', models.BooleanField(default=False)),
                ('salary_paid', models.BooleanField(default=False)),
                ('Faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Faculty.faculty')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='department.department')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
