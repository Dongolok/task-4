# Generated by Django 3.0.2 on 2020-01-19 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('imgpath', models.CharField(default='Imagine path', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('logo', models.CharField(max_length=120)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_by_choices', models.CharField(choices=[(1, 'PHONE'), (2, 'FACEBOOK'), (3, 'EMAIL')], default='PHONE', max_length=1)),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='tables.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=120)),
                ('longitude', models.CharField(max_length=120)),
                ('address', models.TextField()),
                ('branches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='tables.Course')),
            ],
        ),
    ]
