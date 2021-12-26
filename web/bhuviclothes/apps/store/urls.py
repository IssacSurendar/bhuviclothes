from django.urls import path, include
from apps.store import views


urlpatterns = [
    path('<slug:category_slug>/', views.Store, name='products_by_category')
]