from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

""" This is the all products shop page """
def products(request):
    products = Product.objects.all()

    # Pagination on all products page
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = { 'products': paged_products, 'products_all': products }
    return render(request, 'products/products.html', context)

""" This is the for singular product information page """
def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    category = Category.objects.all().filter(name=True)
    context = {'product': product, 'category': category}
    return render(request, "products/product.html", context)
