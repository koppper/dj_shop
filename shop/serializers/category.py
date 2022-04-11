from rest_framework import serializers
from rest_framework.validators import ValidationError

from shop.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'name',
        )
