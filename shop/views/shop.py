from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from shop.models import Shop
from shop.serializers import (
                              ShopSerializer
                              )


class ShopViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
