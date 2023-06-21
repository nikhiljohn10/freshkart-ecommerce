from django.db import models
from shop.models import Product


# Create your models here.
class Cart(models.Model):
    """Model definition for Cart."""

    cart_id = models.CharField(max_length=250)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        """Meta definition for Cart."""

        verbose_name = "Cart"
        verbose_name_plural = "Carts"

        db_table = "Cart"
        ordering = ["date_added"]

    def __str__(self):
        """Unicode representation of Cart."""
        return "{}".format(self.cart_id)


class CartItem(models.Model):
    """Model definition for CartItem."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        """Meta definition for CartItem."""

        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

        db_table = "CartItem"

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        """Unicode representation of CartItem."""
        return "{}".format(self.product.name)
