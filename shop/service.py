from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

from .models import Goods, Category, Shop


class PaginationGood(PageNumberPagination):
    page_size = 5
    max_page_size = 1000


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_FORWARD_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class PaginationCategory(PageNumberPagination):
    page_size = 5
    max_page_size = 1000


class PaginationShop(PageNumberPagination):
    page_size = 5
    max_page_size = 1000
