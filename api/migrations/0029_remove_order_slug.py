# Generated by Django 4.2.1 on 2023-10-22 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_rename_image_slug_productimage_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='slug',
        ),
    ]
