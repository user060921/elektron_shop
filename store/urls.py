from django.urls import path
from . import views


urlpatterns = [
    path('', views.paginator, name='paginator'),
    path('', views.store_page, name='store'),
    path('category/<slug:category_slug>/', views.store_page, name='product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('ajaxAddProduct/', views.ajax_add_product, name='ajaxAddProduct'),
]
