# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-09-08 17:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=225)),
                ('suite', models.CharField(max_length=125)),
                ('city', models.CharField(max_length=125)),
                ('zipcode', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('catchPhrase', models.CharField(max_length=125)),
                ('bs', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=125)),
                ('ing', models.CharField(max_length=125)),
                ('geo', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='posts.Address')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(db_index=True, max_length=32, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('phone', models.CharField(max_length=25)),
                ('website', models.CharField(max_length=125)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.User'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=2000),
        ),
        migrations.AddField(
            model_name='company',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.User'),
        ),
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.User'),
        ),
    ]
