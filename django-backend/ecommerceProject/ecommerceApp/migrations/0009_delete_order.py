# Generated by Django 4.2.4 on 2023-09-27 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0008_remove_product_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
