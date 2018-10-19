# Generated by Django 2.1.2 on 2018-10-19 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalPermissionHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('user', 'Application user'), ('admin', 'Application admin')),
                'managed': False,
            },
        ),
    ]