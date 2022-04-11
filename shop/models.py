from django.db import models


class Shop(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Shop Name'
    )
    goods = models.ManyToManyField('Goods')

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
        ordering = ('id',)


class Goods(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Product Name'
    )
    price = models.IntegerField(
        blank=True,
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Goods'
        verbose_name_plural = 'Goods'
        ordering = ('id',)


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Category Name'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id',)
