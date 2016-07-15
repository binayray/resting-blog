# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 14:27
from __future__ import unicode_literals

import apps.blogs.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to=apps.blogs.models.get_file_path)),
                ('body', models.CharField(max_length=5000)),
                ('slug', models.SlugField()),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
