from django.db.models import Q
from django.shortcuts import redirect, render
from shop.models import Product


def query_result(req):
    products = None
    query = None

    if "q" in req.GET:
        query = req.GET.get("q")
        condition = Q(name__contains=query) | Q(description__contains=query)
        products = Product.objects.all().filter(condition)
        return render(req, "search.html", {"query": query, "products": products})

    return redirect("shop:home")
