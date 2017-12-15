# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-09 17:11
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True, verbose_name='اﻷسم')),
                ('address', models.TextField(verbose_name='العنوان')),
            ],
            options={
                'verbose_name': 'العنوان',
                'verbose_name_plural': 'العناوين',
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_word', models.TextField(verbose_name='كلمه عن الشركه')),
                ('facebook', models.CharField(max_length=300, verbose_name='رابط صفحه الفيس بوك')),
                ('instagram', models.CharField(max_length=300, verbose_name='رابط صفحه الإنستجرام')),
                ('addresses', models.ManyToManyField(to='public.Addresses', verbose_name='العناوين')),
            ],
            options={
                'verbose_name': 'البيانات العامه',
                'verbose_name_plural': 'البيانات العامه',
            },
        ),
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='اﻷسم')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='البريد اﻷلكتروني')),
            ],
            options={
                'verbose_name': 'البريد اﻷلكتروني',
                'verbose_name_plural': 'البريد اﻷلكتروني',
            },
        ),
        migrations.CreateModel(
            name='Mattress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='أسم المرتبه')),
                ('description', models.TextField(verbose_name='وصف المرتبه')),
                ('features', models.TextField(help_text="يجب إدخال كل ميزه مفصول بينها بعلامه ','", verbose_name='المميزات')),
                ('cover', models.ImageField(upload_to='mattress', verbose_name='صوره المرتبه')),
                ('color', models.CharField(max_length=7, verbose_name='لون القائمه')),
                ('is_new', models.BooleanField(default=False, verbose_name='إظهار في الصفحه الرئيسيه')),
                ('stamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'المرتبه',
                'verbose_name_plural': 'المراتب',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='أسم المنتج')),
                ('description', models.TextField(verbose_name='مواصفات المنتج')),
                ('features', models.TextField(help_text="يجب إدخال كل ميزه مفصول بينها بعلامه ','", verbose_name='المميزات')),
                ('cover', models.ImageField(upload_to='product', verbose_name='صوره المنتج')),
                ('color', models.CharField(max_length=7, verbose_name='لون القائمه')),
                ('is_new', models.BooleanField(default=False, verbose_name='إظهار في الصفحه الرئيسيه')),
                ('stamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'المنتج',
                'verbose_name_plural': 'المنتجات',
            },
        ),
        migrations.CreateModel(
            name='Telephones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True, verbose_name='أسم رقم الهاتف')),
                ('number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='لابد ان يكون رقم هاتف حقيقي', regex='^\\+?1?\\d{9,15}$')], verbose_name='رقم الهاتف')),
            ],
            options={
                'verbose_name': 'الهاتف',
                'verbose_name_plural': 'أرقام الهاتف',
            },
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='emails',
            field=models.ManyToManyField(to='public.Emails', verbose_name='البريد اﻷلكتروني'),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='telephones',
            field=models.ManyToManyField(to='public.Telephones', verbose_name='الهواتف'),
        ),
    ]
