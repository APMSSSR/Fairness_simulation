# Generated by Django 3.0 on 2020-01-03 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_auto_20200102_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='interest_change_down',
            field=models.FloatField(default=-0.01),
        ),
        migrations.AddField(
            model_name='bank',
            name='interest_change_up',
            field=models.FloatField(default=0.01),
        ),
    ]