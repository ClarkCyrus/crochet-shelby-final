# Generated by Django 5.0.4 on 2024-05-12 16:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cartitem_additional_notes_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='shipping_fee',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
