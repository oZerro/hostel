# Generated by Django 4.0.6 on 2022-07-28 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otchet', '0004_alter_room_options_alter_spendingadmin_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='room_number',
        ),
        migrations.AddField(
            model_name='profile',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile', to='otchet.room', verbose_name='Комната'),
        ),
    ]
