# Generated by Django 4.0 on 2021-12-31 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('jobboard', '0004_alter_posting_job_email_alter_posting_job_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='author',
            field=models.ForeignKey(default='unna3', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
