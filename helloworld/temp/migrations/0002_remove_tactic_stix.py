# Generated by Django 2.2.12 on 2021-06-11 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tactic',
            name='stix',
        ),
    ]
