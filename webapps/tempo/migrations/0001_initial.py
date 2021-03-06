# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 23:06
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=140)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('zipcode', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('age', models.IntegerField(blank=True, default=1, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
