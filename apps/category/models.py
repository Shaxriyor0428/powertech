from django.db import models
from common.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
