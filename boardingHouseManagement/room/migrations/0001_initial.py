# Generated by Django 5.0.1 on 2024-03-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomsNumber', models.IntegerField()),
                ('acreage', models.IntegerField()),
                ('interior', models.TextField()),
            ],
        ),
    ]
