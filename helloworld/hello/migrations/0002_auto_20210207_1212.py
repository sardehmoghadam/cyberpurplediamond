# Generated by Django 2.2.14 on 2021-02-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.IntegerField(),
        ),
    ]
