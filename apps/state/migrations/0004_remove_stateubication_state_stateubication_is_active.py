# Generated by Django 4.0.4 on 2023-01-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0003_alter_stateubication_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stateubication',
            name='state',
        ),
        migrations.AddField(
            model_name='stateubication',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
    ]
