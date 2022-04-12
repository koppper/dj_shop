from rest_framework import serializers
from rest_framework.validators import ValidationError

from shop.models import Goods, Category
from .category import CategorySerializer, CategoryCreateSerializer


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer

    class Meta:
        model = Goods
        fields = (
            'id',
            'name',
            'price',
            'shop',
            'updated_at',
            'category',
            'update_counter'
        )

    def create(self, validated_data):
        return Goods.objects.create(**validated_data)

#
# class GoodsCreateSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Goods
#         fields = (
#             'name',
#             'price',
#             'shop',
#             'category'
#         )
#
#
# class GoodsUpdateSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(required=False)
#
#     class Meta:
#         model = Goods
#         fields = (
#             'name',
#             'price',
#             'shop',
#             'category'
#         )

    # def update(self, instance, validated_data):
    #     if 'category' in validated_data.keys():
    #         category = Category.objects.filter(id=instance.author_id).first()
    #         category_serializer = CategoryCreateSerializer(category)
    #         category_serializer.update(category, dict(validated_data['category']))
    #         del validated_data['category']
    #     return super().update(instance, validated_data)
