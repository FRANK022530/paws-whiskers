# Generated by Django 4.2.6 on 2024-01-31 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0012_alter_order_price_alter_order_quantity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Customer_Order',
        ),
    ]
