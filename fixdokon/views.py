from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from django.db.models import Q


def home_page(request):
    q = request.GET.get('q', None)
    if q is None:
        products = Product.objects.filter(is_available=True)
    else:
        products = Product.objects.filter(is_available=True).filter(Q(product_name__icontains=q))

    context = {
        "products": products
    }
    return render(request, 'home.html', context)

