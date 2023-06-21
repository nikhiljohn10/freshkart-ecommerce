from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path("add/<int:product_id>/", views.add_cart, name="add"),
    path("remove/<int:product_id>/", views.remove_cart, name="remove"),
    path("delete/<int:product_id>/", views.delete_cart, name="delete"),
    path("", views.cart_home, name="home"),
]
