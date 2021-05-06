from django.shortcuts import render
from .models import Supplier, Product


def landingview(request):
    return render (request, "landingpage.html")

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'supplier': supplierlist}
    return render (request, "supplier.html", context)



def productlistview(request):
    productlist = Product.objects.all()
    context = {'product': productlist}
    return render (request, "product.html", context)