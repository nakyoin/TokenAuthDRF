# Generated by Django 4.1.7 on 2023-03-28 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_rename_newornot_product_new_or_not_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=5),
        ),
    ]
