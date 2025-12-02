from django.shortcuts import render
from dbapp2.models import Product
# Create your views here.

def product_data(request):
    prod_list = Product.objects.all()
    product_dict={'prod_list':prod_list}
    return render(request, 'product.html', context=product_dict)
