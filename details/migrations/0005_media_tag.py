# Generated by Django 3.2.7 on 2021-11-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='tag',
            field=models.CharField(default='bday', max_length=20),
            preserve_default=False,
        ),
    ]
