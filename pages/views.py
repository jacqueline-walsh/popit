from django.shortcuts import render
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()[:3]
    context = {'products': products}
    return render(request, 'pages/index.html', context)