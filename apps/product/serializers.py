from rest_framework import serializers
from apps.category.models import Category
from apps.product.models import ProductImage, ProductCharacteristic, Product, ProductCharacteristicSection


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "image")
        read_only_fields = ("id",)


class CategoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ProductCharacteristicItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCharacteristic
        fields = ("name", "description")


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryNestedSerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "price",
            "image",
            "category",
            "images",
        )



class ProductDetailSerializer(serializers.ModelSerializer):
    specifications = serializers.SerializerMethodField()
    category = CategoryNestedSerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "price",
            "specifications",
            "category",
            "images",
        )

    def get_specifications(self, obj):
        """
        Return characteristics grouped by section (global sections allowed).
        """
        result = []

        # 1️⃣ Section bilan bog‘langan characteristiclar
        sections = ProductCharacteristicSection.objects.prefetch_related(
            "characteristics"
        )

        for section in sections:
            # Faqat shu productga tegishli characteristiclar
            items = section.characteristics.filter(product=obj)
            if not items.exists():
                continue

            result.append({
                "title": section.title,
                "items": ProductCharacteristicItemSerializer(
                    items, many=True
                ).data
            })

        # 2️⃣ Section BO‘LMAGAN characteristiclar
        no_section_items = obj.characteristics.filter(section__isnull=True)
        if no_section_items.exists():
            result.append({
                "title": None,
                "items": ProductCharacteristicItemSerializer(
                    no_section_items, many=True
                ).data
            })

        return result
