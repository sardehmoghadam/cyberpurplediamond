# Generated by Django 2.2.14 on 2021-02-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0005_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='users',
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='Readed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]