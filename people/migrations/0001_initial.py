# Generated by Django 2.2.1 on 2019-05-28 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
            ],
        ),
    ]
