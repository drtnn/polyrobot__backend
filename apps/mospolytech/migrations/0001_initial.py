# Generated by Django 4.0 on 2022-02-06 17:45

import uuid

import django.db.models.deletion
import encrypted_model_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=10, verbose_name='Group Number')),
            ],
            options={
                'verbose_name': 'Учебная группа',
                'verbose_name_plural': 'Учебные группы',
            },
        ),
        migrations.CreateModel(
            name='MospolytechUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('login', models.CharField(max_length=32, verbose_name='Mospolytech Login')),
                ('password', encrypted_model_fields.fields.EncryptedCharField(verbose_name='Mospolytech Password')),
                ('cached_token', models.TextField(verbose_name='Cached Mospolytech Token')),
                ('telegram',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='telegram.telegramuser',
                                      verbose_name='Telegram User')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='Name')),
                ('surname', models.CharField(max_length=16, verbose_name='Surname')),
                ('patronymic', models.CharField(blank=True, max_length=16, null=True, verbose_name='Patronymic')),
            ],
            options={
                'verbose_name': 'Персональные данные',
                'verbose_name_plural': 'Персональные данные',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('groups', models.ManyToManyField(to='mospolytech.Group', verbose_name='Groups')),
                ('personal_data',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mospolytech.personaldata',
                                      verbose_name='Personal Data')),
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mospolytech.mospolytechuser',
                                      verbose_name='User')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mospolytech.group',
                                            verbose_name='Group')),
                ('personal_data',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mospolytech.personaldata',
                                      verbose_name='Personal Data')),
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mospolytech.mospolytechuser',
                                      verbose_name='User')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
