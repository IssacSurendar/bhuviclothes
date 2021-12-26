from django.shortcuts import render
from apps.store.models import Product

# Create your views here.
def Home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products':products
    }
    print(products)
    return render(request, 'index.html', context)