# Generated by Django 5.0.1 on 2024-03-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_alter_room_acreage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='roomsNumber',
            field=models.IntegerField(),
        ),
    ]
