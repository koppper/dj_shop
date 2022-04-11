from django.urls import path
from rest_framework.routers import DefaultRouter

from shop.views import GoodsViewSet, ShopViewSet

router = DefaultRouter()
router.register('goods', GoodsViewSet)
router.register('shops', ShopViewSet)
urlpatterns = [
    # path('shops/', ShopViewSet),

] + router.urls
