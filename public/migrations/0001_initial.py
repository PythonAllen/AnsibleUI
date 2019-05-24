# Generated by Django 2.2.1 on 2019-05-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnsibleTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AnsibleID', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('CeleryID', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('GroupName', models.CharField(blank=True, max_length=80, null=True)),
                ('playbook', models.CharField(blank=True, max_length=80, null=True)),
                ('AnsibleResult', models.TextField(blank=True)),
                ('CeleryResult', models.TextField(blank=True)),
            ],
        ),
    ]
