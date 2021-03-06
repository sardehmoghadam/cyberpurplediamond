# Generated by Django 2.2.12 on 2021-06-08 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=4096)),
                ('reference', models.CharField(max_length=2048)),
                ('stix', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('reference', models.CharField(max_length=128)),
                ('img', models.ImageField(upload_to='')),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('totalread', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='contactmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('subject', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=1024)),
                ('readed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='malware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=4096)),
                ('reference', models.CharField(max_length=2048)),
                ('stix', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='maxview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.IntegerField()),
                ('postview', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mitigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=4096)),
                ('stix', models.CharField(max_length=512)),
                ('reference', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='refer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TACTIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=4096)),
                ('reference', models.CharField(max_length=2048)),
                ('stix', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=4096)),
                ('reference', models.CharField(max_length=2048)),
                ('stix', models.CharField(max_length=512)),
                ('rel_actor', models.ManyToManyField(to='temp.actor')),
            ],
        ),
        migrations.CreateModel(
            name='technique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=4096)),
                ('platform', models.CharField(max_length=128)),
                ('permission', models.CharField(max_length=512)),
                ('commandlist', models.CharField(blank=True, max_length=4096)),
                ('command_ref', models.CharField(blank=True, max_length=4096)),
                ('dataset', models.CharField(blank=True, max_length=4096)),
                ('datasource', models.CharField(blank=True, max_length=4096)),
                ('possible_detection', models.CharField(blank=True, max_length=4096)),
                ('rel_actor', models.ManyToManyField(to='temp.actor')),
                ('rel_malware', models.ManyToManyField(to='temp.malware')),
                ('rel_mitigation', models.ManyToManyField(to='temp.mitigation')),
                ('rel_tactic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temp.TACTIC')),
            ],
        ),
        migrations.CreateModel(
            name='subtechnique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=2048, null=True)),
                ('platform', models.CharField(max_length=128, null=True)),
                ('rel_actor', models.ManyToManyField(to='temp.actor')),
                ('rel_malware', models.ManyToManyField(to='temp.malware')),
                ('rel_mitigation', models.ManyToManyField(to='temp.mitigation')),
                ('rel_technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temp.technique')),
            ],
        ),
    ]
