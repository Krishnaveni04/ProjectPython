# Generated by Django 4.1.7 on 2023-04-11 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_products_cartitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
