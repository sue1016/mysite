# Generated by Django 2.0.2 on 2019-05-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0007_auto_20190503_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Cara Sue', max_length=255)),
                ('maintenance_mode', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'ChatBot',
            },
        ),
    ]