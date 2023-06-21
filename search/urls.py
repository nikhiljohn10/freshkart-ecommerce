from django.urls import path

from . import views

app_name = "search"
urlpatterns = [
    path("", views.query_result, name="query"),
]
