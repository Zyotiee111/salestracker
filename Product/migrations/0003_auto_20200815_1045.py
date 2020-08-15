# Generated by Django 3.1 on 2020-08-15 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='totalprofit',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='totalsale',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
