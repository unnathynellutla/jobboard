# Generated by Django 4.0 on 2022-01-01 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0003_stage_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='author',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='order',
        ),
    ]