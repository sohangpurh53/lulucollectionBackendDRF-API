# Generated by Django 4.2.1 on 2024-04-06 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_product_colors_product_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
    ]