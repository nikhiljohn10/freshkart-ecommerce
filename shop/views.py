from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def home(req, c_slug=None):
    c_page = None
    # products = None
    product_list = None

    if not c_slug is None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product_list = Product.objects.all().filter(category=c_page, available=True)
    else:
        product_list = Product.objects.all().filter(available=True)

    paginator = Paginator(product_list, 6)

    try:
        page = int(req.GET.get("page", "1"))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(req, "home.html", {"category": c_page, "products": products})


def detail(req, c_slug: str, p_slug: str):
    context = {}
    try:
        product = Product.objects.get(category__slug=c_slug, slug=p_slug)
        context["product"] = product
    except Exception as e:
        raise e
    return render(req, "product.html", context)
