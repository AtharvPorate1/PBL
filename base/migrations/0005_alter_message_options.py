# Generated by Django 4.0.3 on 2022-07-11 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_partictipants_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
