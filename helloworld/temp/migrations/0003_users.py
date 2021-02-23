# Generated by Django 2.2.14 on 2021-02-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0002_auto_20210213_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64)),
                ('key', models.CharField(max_length=1024)),
                ('salt', models.CharField(max_length=1024)),
            ],
        ),
    ]