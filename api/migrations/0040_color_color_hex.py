# Generated by Django 4.2.1 on 2024-04-13 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_style_product_size_cartitem_style_product_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='color_hex',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
