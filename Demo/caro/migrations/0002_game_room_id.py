# Generated by Django 3.0.7 on 2020-06-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='room_id',
            field=models.IntegerField(default=0),
        ),
    ]