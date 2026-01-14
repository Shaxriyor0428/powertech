from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from apps.category.models import Category
from apps.category.serializers import CategorySerializer


class CategoryViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Category.objects.all().order_by("-created_at")
    http_method_names = ["get", "post", "patch", "delete"]
    serializer_class = CategorySerializer

