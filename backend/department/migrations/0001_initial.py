# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-31 17:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('short_code', models.CharField(max_length=4)),
                ('about_us', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Electives',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_code', models.CharField(max_length=7)),
                ('title', models.CharField(max_length=200)),
                ('is_open', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Departments')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('research_interest', models.TextField()),
                ('email', models.CharField(default='', max_length=255)),
                ('mobile', models.IntegerField()),
                ('joining_year', models.DateField(default=datetime.datetime(2018, 1, 31, 17, 54, 42, 407353))),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Departments')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Departments')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('collab_inst', models.TextField()),
                ('area', models.CharField(max_length=255)),
                ('faculty_involved', models.TextField()),
                ('date', models.DateField(default=datetime.datetime(2018, 1, 31, 17, 54, 42, 408643))),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Departments')),
            ],
        ),
    ]