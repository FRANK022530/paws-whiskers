# Generated by Django 4.2.6 on 2024-01-31 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_cart_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Total',
        ),
    ]
