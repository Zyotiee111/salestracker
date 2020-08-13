# Generated by Django 3.1 on 2020-08-13 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default=None, max_length=255)),
                ('quantity', models.IntegerField()),
                ('totalsale', models.IntegerField()),
                ('capital_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
                ('totalprofit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
