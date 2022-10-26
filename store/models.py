from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=180)
    web_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=180)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True, related_name="store")
    sku = models.CharField(max_length=180)
    brand = models.CharField(max_length=180)
    type=models.CharField(max_length=180)
    size = models.CharField(max_length=180, null=True)
    image_url = models.CharField(max_length=280)
    price = models.FloatField()


