# Generated by Django 2.0.3 on 2018-03-10 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_sku_subcategory_subcategory_sku'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
