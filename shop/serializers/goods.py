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
            'updated_at',
            'category'
        )


class GoodsCreateSerializer(serializers.ModelSerializer):
    category = CategorySerializer

    class Meta:
        model = Goods
        fields = (
            'name',
            'price'
            'category'
        )

    def create(self, validated_data):
        category = validated_data['category']
        new_category_data = {'name': category['name']}

        if new_category_data:
            new_category = CategoryCreateSerializer(data=new_category_data)
            new_category.is_valid(raise_exception=True)
            new_category.save()
            validated_data['category'] = new_category.instance
        return super().create(validated_data)


class GoodsUpdateSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)

    class Meta:
        model = Goods
        fields = (
            'name',
            'price'
            'category'
        )

    def update(self, instance, validated_data):
        if 'category' in validated_data.keys():
            category = Category.objects.filter(id=instance.author_id).first()
            category_serializer = CategoryCreateSerializer(category)
            category_serializer.update(category, dict(validated_data['category']))
            del validated_data['category']
        return super().update(instance, validated_data)
