# Generated by Django 4.2.6 on 2024-01-31 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0011_alter_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='Quantity',
            field=models.IntegerField(),
        ),
    ]