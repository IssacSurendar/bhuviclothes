from django.urls import path, include
from apps.store import views


urlpatterns = [
    path('', views.Store, name='store'),
    path('<slug:category_slug>/', views.FilterByCategory, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductDetail, name='product_detail'),
    path('search', views.Search, name='search')
]
