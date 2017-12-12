# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 23:42
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tempo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_info', models.TextField(blank=True, max_length=140)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('zipcode', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('created_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='tempo/media')),
            ],
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, upload_to='tempo/media'),
        ),
        migrations.AddField(
            model_name='band',
            name='artist',
            field=models.ManyToManyField(related_name='member', to='tempo.Artist'),
        ),
        migrations.AddField(
            model_name='band',
            name='band_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='band', to=settings.AUTH_USER_MODEL),
        ),
    ]
