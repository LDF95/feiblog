# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-22 09:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u59d3\u540d')),
                ('desc', models.TextField(max_length=500, verbose_name='\u7b80\u4ecb')),
                ('profession', models.CharField(max_length=50, verbose_name='\u4e13\u4e1a')),
                ('year', models.CharField(choices=[('1', '2018\u5e74'), ('2', '2017\u5e74'), ('3', '2016\u5e74'), ('4', '2015\u5e74')], default='1', max_length=10, verbose_name='\u5e74\u4efd')),
            ],
            options={
                'verbose_name': '\u4f5c\u8005',
                'verbose_name_plural': '\u4f5c\u8005',
            },
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('desc', models.CharField(max_length=100, verbose_name='\u63cf\u8ff0')),
                ('content', models.TextField(max_length=50000, verbose_name='\u5185\u5bb9')),
                ('image', models.ImageField(upload_to='blog/%Y/%m', verbose_name='\u5c01\u9762')),
                ('direction', models.CharField(max_length=50, verbose_name='\u65b9\u5411')),
                ('category', models.CharField(choices=[('t1', 'CCIE\u7f51\u7edc'), ('t2', 'Linux\u7cfb\u7edf'), ('t3', 'Python\u5165\u95e8'), ('t4', 'Web\u5b89\u5168'), ('t5', 'Django\u6846\u67b6'), ('t6', '\u6570\u636e\u5e93'), ('t7', '\u524d\u7aef'), ('t8', '\u5176\u4ed6')], default='t1', max_length=10, verbose_name='\u7c7b\u522b')),
                ('pub_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('read_counts', models.IntegerField(default=0, verbose_name='\u9605\u8bfb\u6b21\u6570')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author', verbose_name='\u6240\u5c5e\u4f5c\u8005')),
            ],
            options={
                'verbose_name': '\u535a\u6587',
                'verbose_name_plural': '\u535a\u6587',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='\u59d3\u540d')),
                ('email', models.CharField(max_length=50, verbose_name='\u90ae\u7bb1')),
                ('password', models.CharField(max_length=128, verbose_name='\u5bc6\u7801')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5')),
                ('gender', models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], default='male', max_length=10, verbose_name='\u6027\u522b')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m', verbose_name='\u5934\u50cf')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]