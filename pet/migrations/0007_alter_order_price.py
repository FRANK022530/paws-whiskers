# Generated by Django 4.2.6 on 2024-01-31 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_alter_order_customername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
