from django.db import models
from apps.category.models import Category
from common.base_model import BaseModel


class Product(BaseModel):
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=18, decimal_places=2)
    image = models.ImageField("Основное изображение", upload_to="products/", blank=True, null=True)

    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )

    class Meta:
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class ProductCharacteristicSection(BaseModel):
    """
    Раздел / заголовок характеристик (может быть общим для товаров)
    """
    title = models.CharField("Название раздела", max_length=255, unique=True)

    class Meta:
        db_table = "product_characteristic_sections"
        verbose_name = "Раздел характеристик"
        verbose_name_plural = "Разделы характеристик"

    def __str__(self):
        return self.title


class ProductCharacteristic(BaseModel):
    product = models.ForeignKey(
        Product,
        verbose_name="Товар",
        on_delete=models.CASCADE,
        related_name="characteristics"
    )
    section = models.ForeignKey(
        ProductCharacteristicSection,
        verbose_name="Раздел",
        on_delete=models.SET_NULL,
        related_name="characteristics",
        blank=True,
        null=True
    )
    name = models.CharField("Название характеристики", max_length=555)
    description = models.TextField("Описание", blank=True, null=True)

    class Meta:
        db_table = "product_characteristics"
        verbose_name = "Характеристика товара"
        verbose_name_plural = "Характеристики товара"

    def __str__(self):
        section_title = self.section.title if self.section else "Без раздела"
        return f"{section_title} — {self.name}"


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product,
        verbose_name="Товар",
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField("Изображение", upload_to="product_images/")

    class Meta:
        db_table = "product_images"
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товара"

    def __str__(self):
        return f"Изображение товара: {self.product.title}"
