from django.shortcuts import render
from products.models import Product
from category.models import Category

# Create your views here.
def search(request):
    queryset_list = Product.objects.order_by('-id')

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        print(price)
        if price == 'descending':
            queryset_list = queryset_list.order_by('-price')
        elif price == 'ascending': 
            queryset_list = queryset_list.order_by('price')

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__name__exact=category)

    # Search all
    queryset_list = queryset_list.filter(name__icontains=request.GET['q'])

    context = {
        'products': queryset_list,
        'values': request.GET
    }

    return render(request,  "products/products.html", context)
