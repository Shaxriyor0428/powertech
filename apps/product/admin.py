from django.contrib import admin
from django.utils.html import format_html

from apps.product.models import ProductImage, ProductCharacteristicSection
from apps.product.models.product import Product, ProductCharacteristic


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "image_preview")
    list_filter = ("product",)
    search_fields = ("product__title",)
    readonly_fields = ("image_preview",)
    ordering = ("-created_at",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:100px;border-radius:6px;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Изображение"


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    verbose_name = "Изображение товара"
    verbose_name_plural = "Изображения товара"


class ProductCharacteristicInline(admin.TabularInline):
    model = ProductCharacteristic
    extra = 1
    fields = ("section", "name", "description")
    verbose_name = "Характеристика товара"
    verbose_name_plural = "Характеристики товара"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "image_preview", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "description")
    ordering = ("-created_at",)
    list_per_page = 25

    readonly_fields = ("image_preview", "created_at", "updated_at")

    fieldsets = (
        ("Данные товара", {
            "fields": (
                "title",
                "description",
                "category",
                "price",
                "image",
                "image_preview",
            )
        }),
        ("Дата и время", {
            "fields": ("created_at", "updated_at")
        }),
    )

    inlines = (ProductImageInline, ProductCharacteristicInline)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:80px;border-radius:6px;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Изображение"


@admin.register(ProductCharacteristic)
class ProductCharacteristicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "section", "created_at")
    list_filter = ("section", "created_at")
    search_fields = ("name", "description", "section__title", "product__title")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(ProductCharacteristicSection)
class ProductCharacteristicSectionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
    ordering = ("-created_at",)
    inlines = (ProductCharacteristicInline,)
