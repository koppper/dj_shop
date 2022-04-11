from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Shop Name')
    goods = models.ManyToManyField('Goods')

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Product Name')
    price = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Category Name')

    def __str__(self):
        return self.name
