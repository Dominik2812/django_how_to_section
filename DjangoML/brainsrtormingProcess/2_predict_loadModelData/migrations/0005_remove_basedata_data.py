# Generated by Django 3.1.3 on 2021-04-12 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0004_auto_20210412_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basedata',
            name='data',
        ),
    ]
