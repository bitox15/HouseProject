# Generated by Django 4.0.4 on 2022-11-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basemodel',
            name='state',
            field=models.BooleanField(default=True, verbose_name='state'),
        ),
    ]
