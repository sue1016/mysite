# Generated by Django 2.0.2 on 2019-05-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0006_auto_20190503_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='hasDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='hasDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
