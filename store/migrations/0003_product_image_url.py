# Generated by Django 4.0.4 on 2022-05-17 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_category_store_id_remove_product_list_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(default='', max_length=180),
            preserve_default=False,
        ),
    ]
