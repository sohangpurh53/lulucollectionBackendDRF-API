# Generated by Django 4.2.1 on 2024-04-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_remove_product_colors_remove_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, null=True, to='api.color'),
        ),
    ]