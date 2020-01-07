from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def products(request):
    products = Product.objects.all()
    context = { 'products': products }
    return render(request, 'products/products.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    category = Category.objects.all().filter(name=True)
    context = {'product': product, 'category': category}
    return render(request, "products/product.html", context)
