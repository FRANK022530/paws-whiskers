# Generated by Django 4.2.6 on 2024-01-31 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0010_alter_cart_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Price',
            field=models.CharField(max_length=50),
        ),
    ]