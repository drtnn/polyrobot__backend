# Generated by Django 4.0 on 2022-02-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonteacher',
            name='full_name',
            field=models.CharField(max_length=48, verbose_name='Lesson Teacher'),
        ),
    ]
