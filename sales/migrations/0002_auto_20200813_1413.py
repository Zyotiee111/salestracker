# Generated by Django 3.1 on 2020-08-13 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='description',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(),
        ),
    ]
