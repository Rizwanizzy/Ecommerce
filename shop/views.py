from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def index(request, c_slug=None):
    c_page = None
    prod = None
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prod = product.objects.filter(category=c_page, availability=True)
    else:
        prod = product.objects.all().filter(availability=True)
    cat = categ.objects.all()

    paginator = Paginator(prod, 3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'prod': prod, 'cat': cat, 'pg': pro})


def product_details(request, c_slug, p_slug):
    try:
        prod = product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'prod': prod})


def search(request):
    prod = None
    query = None
    if "q" in request.GET:
        query = request.GET.get("q")
        prod = product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))

    return render(request, 'search.html', {'query': query, 'prod': prod})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def faqs(request):
    return render(request, 'faqs.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')
