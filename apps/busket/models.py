from django.db import models
from apps.product.models.product import Product
from apps.users.models import User
from common.base_model import BaseModel


class Busket(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="buskets"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='buskets')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    class Meta:
        db_table = "buskets"
        verbose_name = "Busket"
        verbose_name_plural = "Buskets"

    def __str__(self):
        return f"Busket of {self.user.username}"