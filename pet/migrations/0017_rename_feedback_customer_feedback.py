# Generated by Django 4.2.6 on 2024-02-01 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0016_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='feedback',
            new_name='Customer_feedback',
        ),
    ]