# Generated by Django 4.0.5 on 2022-09-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otchet', '0025_alter_profile_room'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-room'], 'verbose_name': 'Постоялец', 'verbose_name_plural': 'Постояльцы'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['number'], 'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
        migrations.AddField(
            model_name='departures',
            name='room',
            field=models.CharField(max_length=3, null=True, verbose_name='Номер комнаты'),
        ),
    ]