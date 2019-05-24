# Generated by Django 2.2.1 on 2019-05-14 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Functions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcName', models.CharField(blank=True, max_length=80, null=True)),
                ('nickName', models.CharField(blank=True, max_length=80, null=True)),
                ('playbook', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostsLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostName', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('hostAddr', models.CharField(max_length=80, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('nickName', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('remark', models.TextField(blank=True)),
                ('hostList', models.ManyToManyField(to='public.HostsLists')),
                ('possessFuncs', models.ManyToManyField(to='public.Functions')),
            ],
        ),
    ]
