from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from shop.models import Category
from shop.serializers import (CategorySerializer, CategoryCreateSerializer)


class CatViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_serializer_class(self):
        serializer_class = CategorySerializer

        if self.action == 'create':
            serializer_class = CategoryCreateSerializer
        return serializer_class
