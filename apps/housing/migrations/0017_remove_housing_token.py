# Generated by Django 4.0.4 on 2023-01-12 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0016_housing_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housing',
            name='token',
        ),
    ]