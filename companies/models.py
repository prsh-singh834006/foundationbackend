from django.db import models

# Create your models here.
class Subcategory(models.Model):
    sub_category_id = models.IntegerField(primary_key=True)
    sub_category_name = models.CharField(max_length=100)
class Sku(models.Model):
    sku_id = models.IntegerField(primary_key=True)
    sku_description = models.CharField(max_length=500)
class Subcategory_SKU(models.Model):
    sub_category_id = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    sku_id = models.ForeignKey(Sku,on_delete=models.CASCADE)
