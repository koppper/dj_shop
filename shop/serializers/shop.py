from rest_framework import serializers
from rest_framework.validators import ValidationError

from shop.models import Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = (
            'id',
            'name',
            'goods'
        )

