from django.db import models


class Shop(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Shop Name'
    )

    def __str__(self):
        return self.name

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
        on_delete=models.DO_NOTHING
    )
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE
    )

    update_counter = models.IntegerField(
        default=0
    )

    def save(self, *args, **kwargs):
        self.update_counter += 1
        super(Goods, self).save(*args, **kwargs)

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id',)
