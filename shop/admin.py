from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin View for Category"""

    list_display = (
        "name",
        "slug",
    )
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin View for Product"""

    list_display = (
        "name",
        "slug",
        "price",
        "stock",
        "available",
        "created",
        "updated",
    )
    list_editable = ["price", "stock", "available"]
    list_per_page = 20
    prepopulated_fields = {"slug": ("name",)}
