from django.shortcuts import render, get_object_or_404
from .models import *


def index(request, c_slug=None):
    c_page = None
    prod = None
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prod = product.objects.filter(category=c_page, availability=True)
    else:
        prod = product.objects.all().filter(availability=True)
    cat = categ.objects.all()
    return render(request, 'index.html', {'prod': prod, 'cat': cat})


def product_details(request, c_slug, p_slug):
    try:
        prod = product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'prod': prod})
