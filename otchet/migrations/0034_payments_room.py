# Generated by Django 4.1.1 on 2022-09-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otchet', '0033_profile_room_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='room',
            field=models.CharField(max_length=3, null=True, verbose_name='Номер комнаты'),
        ),
    ]
