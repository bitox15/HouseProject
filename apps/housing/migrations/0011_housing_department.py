# Generated by Django 4.0.4 on 2022-11-22 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0002_alter_stateubication_options'),
        ('housing', '0010_alter_housing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='state.stateubication'),
        ),
    ]
