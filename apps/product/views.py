from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.product.models.product import Product
from apps.product.serializers import ProductListSerializer, ProductDetailSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        return ProductDetailSerializer

    queryset = (
        Product.objects
        .select_related("category")
        .prefetch_related(
            "images",
            "characteristics",
        )
        .order_by("-created_at")
    )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="category_id",
                description="Filter products by category ID",
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        category_id = request.query_params.get("category_id", None)

        queryset = self.queryset
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
