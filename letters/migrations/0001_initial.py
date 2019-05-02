# Generated by Django 2.0.2 on 2019-05-02 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_md', models.CharField(max_length=20000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('pub_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letters.Author')),
            ],
        ),
    ]
