# Generated by Django 4.0.5 on 2022-09-10 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otchet', '0022_remove_departures_user_departures_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='departures',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='otchet.profile', verbose_name='Имя'),
        ),
    ]
