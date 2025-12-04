from django.shortcuts import render, redirect
from prodapp.forms import ProductForm
from prodapp.models import Product
# Create your views here.

def getcreateprod(request):
    if request.method == 'POST':
        prod_data=ProductForm(request.POST)
        if prod_data.is_valid():
            try:
                prod_data.save()
                return redirect('/read')
            except:
                pass
    else:
        prodform=ProductForm()
    return render(request, 'create.html', {'form':prodform})

def getreadprod(request):
    products=Product.objects.all()
    return render(request, 'read.html', {'products':products})

def getupdateprod(request, id):
    product=Product.objects.get(id=id)
    if request.method == 'POST':
        product.pid = request.POST.get('pid')
        product.pname = request.POST.get('pname')
        product.price = request.POST.get('price')
        product.qty = request.POST.get('qty')
        product.save()
        return redirect('/read')
    return render(request, 'update.html', {'product':product})

def getdeleteprod(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('/read')