from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)

class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    default = 1

class ProductPageNumberPagination(PageNumberPagination):
    page_size = 1