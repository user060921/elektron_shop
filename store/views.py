from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.db.models import Q
from django.core.paginator import Paginator

def paginator(request):
    products = Product.objects.all()
    p = Paginator(products,3)
    page = request.GET.get('page')
    context = {
        'products':p.get_page(page)
    } 

    return render(request, 'store/store.html', context)

def store_page(request, category_slug=None):
    
    q = request.GET.get('q', None)
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        p = Product.objects.filter(category=category, is_available=True)
        p_count = p.count()
    else:
        p = Product.objects.filter(is_available=True)
        p_count = p.count()
    if q is not None:
        products = products.filter(Q(product_name__icontains=q))
        p_count = p.count()
    context = {
        "p": p,
        "p_count": p_count,
    }
    return render(request, 'store/store.html', context)




def product_detail(request, category_slug, product_slug):
    product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    context = {
        "product": product,
    }
    return render(request, 'store/product_detail.html', context)


def ajax_add_product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        color = request.GET.get('color')
        size = request.GET.get('size')
        print(product_id, color, size)
        return HttpResponse("True")

