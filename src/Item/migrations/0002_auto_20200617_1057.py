# Generated by Django 3.0.7 on 2020-06-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='voiceNote',
            field=models.FileField(max_length=150, upload_to=''),
        ),
    ]
