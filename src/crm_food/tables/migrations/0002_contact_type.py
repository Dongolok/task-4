# Generated by Django 3.0.2 on 2020-01-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='type',
            field=models.CharField(default='', max_length=100),
        ),
    ]