from django.db import models
from apps.category.models import Category
from common.base_model import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="products"
    )

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title


class ProductCharacteristicSection(BaseModel):
    """
    Reusable Section/heading for characteristics. Optional.
    """
    title = models.CharField(max_length=255, unique=True)  # UNIQUE bo‘lsa global

    class Meta:
        db_table = "product_characteristic_sections"
        verbose_name = "Product Characteristic Section"
        verbose_name_plural = "Product Characteristic Sections"

    def __str__(self):
        return self.title


class ProductCharacteristic(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="characteristics"
    )
    section = models.ForeignKey(
        ProductCharacteristicSection,
        on_delete=models.SET_NULL,
        related_name="characteristics",
        blank=True,
        null=True
    )
    name = models.CharField(max_length=555)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "product_characteristics"
        verbose_name = "Product Characteristic"
        verbose_name_plural = "Product Characteristics"

    def __str__(self):
        section_title = self.section.title if self.section else "No Section"
        return f"{section_title} - {self.name}"


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="product_images/")

    class Meta:
        db_table = "product_images"
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return f"Image of {self.product.title}"
