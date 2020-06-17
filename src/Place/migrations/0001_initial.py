# Generated by Django 3.0.7 on 2020-06-17 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(default=' ')),
                ('dates', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('created', models.DateTimeField()),
            ],
        ),
    ]