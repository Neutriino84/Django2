from django.shortcuts import render,redirect
from .models import Supplier, Product 
from django.contrib.auth import authenticate, login, logout

# landing after login
'''
def landingview(request):
    return render (request, "landingpage.html")
    '''


# Login and Logout

def loginview(request):
    return render (request, "logingpage.html")


def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username = user, password = passw)
    if user:
        login(request, user)
        context = ('name', user)
        return render(request, 'landingpage.html', context)
    else:
        return render(request, 'loginerror.html')

def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')



# supplier handling amd view functions.

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'supplier': supplierlist}
    return render (request, "supplier.html", context)

    
def edit_supplier_get(request, iidee):
    supplier = Supplier.objects.filter(id = iidee)
    context = {'supplier': Product}
    return render (request,"edit_product.html", context)

def edit_supplier_post(request, iidee):
    item =Supplier.objects.get(id = iidee)
    item.contactname = request.POST['contactname']
    item.address = request.POST['address']
    item.phone = request.POST['phone']
    item.email = request.POST['email']
    item.country = request.POST['country']
    item.save()
    return redirect(supplierlistview)

def addsupplier(request):
    a = request.POst['companyname']
    b = request.POst['contactname']
    c = request.POst['address']
    d = request.POst['phone']
    e = request.POst['email']
    f = request.POst['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = 
    e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def deletesupplier(request,iidee):
    Supplier.objects.filter(id = iidee).delete()
    return redirect(request.META['HTTP_REFERER'])

def edit_supplier_get(request, iidee):
    Supplier.objects.filter(id = iidee)
    context = {'supplier': Supplier}
    return render (request,"edit_supplier.html", context)
# products handling and view functions.

def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        context = {'products': productlist}
        return render (request, "products.html", context)

def addproduct(request):
    a = request.POst['productname']
    b = request.POst['packagesize']
    c = request.POst['unitprice']
    d = request.POst['unitsinstock']
    e = request.POst['companyname']
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, companyname = e).save()
    return redirect(request.META['HTTP_REFERER'])
 

def deleteproduct(request, iidee):
    Product.objects.filter(id = iidee).delete()
    return redirect(request.META['HTTP_REFERER'])

def edit_product_get(request, iidee):
    product = Product.objects.filter(id = iidee)
    context = {'product': product}
    return render (request,"edit_product.html", context)

def edit_product_post(request, iidee):
    item = Product.objects.get(id = iidee)
    item.unitprice = request.POST['unitprice']
    item.unitsinstock = request.POST['unitsinstock']
    item.save()
    return redirect(productlistview)

def products_filtered(request, iidee):
    supplierobj = Supplier.objects.get(id = iidee)
    cname = supplierobj.companyname
    
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(companyname = cname)
    context = {'products': filteredproducts}
    return render (request,"products.html",context)