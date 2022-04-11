
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from shop.models import Goods
from shop.serializers import (GoodsUpdateSerializer,
                              GoodsCreateSerializer,
                              GoodsSerializer
                              )


class GoodsViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()

    # def get_serializer_class(self):
    #     serializer_class = GoodsSerializer
    #
    #     if self.action == 'create':
    #         serializer_class = GoodsCreateSerializer
    #     elif self.action == 'update':
    #         serializer_class = GoodsUpdateSerializer
    #
    #     return serializer_class
