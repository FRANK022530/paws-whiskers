# Generated by Django 4.2.6 on 2024-01-31 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0005_remove_order_order_id_order_customeraddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='CustomerName',
            field=models.CharField(max_length=50),
        ),
    ]