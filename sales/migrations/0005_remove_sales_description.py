# Generated by Django 3.1 on 2020-08-15 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20200814_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='description',
        ),
    ]
