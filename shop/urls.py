from django.urls import path

from . import views

app_name = "shop"
urlpatterns = [
    path("", views.home, name="home"),
    path("<slug:c_slug>/", views.home, name="products_by_category"),
    path("<slug:c_slug>/<slug:p_slug>/", views.detail, name="detail"),
]
