# Generated by Django 3.0.2 on 2020-01-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_auto_20200126_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_by_choices',
            field=models.IntegerField(choices=[(1, 'PHONE'), (2, 'FACEBOOK'), (3, 'EMAIL')]),
        ),
    ]