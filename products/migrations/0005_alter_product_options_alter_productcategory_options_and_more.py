# Generated by Django 4.1.7 on 2023-03-23 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_descripton_product_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='productcategory',
            old_name='descripton',
            new_name='description',
        ),
    ]
