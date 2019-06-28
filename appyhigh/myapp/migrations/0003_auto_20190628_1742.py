# Generated by Django 2.1.7 on 2019-06-28 12:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_food_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_year',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]