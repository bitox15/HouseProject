# Generated by Django 4.0.4 on 2022-11-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0008_housing_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='price',
            field=models.IntegerField(max_length=255, null=True),
        ),
    ]