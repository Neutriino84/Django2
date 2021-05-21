from django.urls import path
from .views import supplierlistview, productlistview, addsupplier, addproduct, deletesupplier, deleteproduct, edit_supplier_get, edit_product_get, edit_product_post, edit_supplier_post, products_filtered, loginview, login_action, logout_action

urlpatterns = [
    # LANDING PAGE AFTER LOGIN
    #path('', landingview),

    # Loginview and authentication method
    path('landing/', loginview),
    path('login/', login_action),
    path('logout/', logout_action),


    # suppliers urls
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:iidee>/',deletesupplier),
    path('edit_supplier_get/int:iidee>/', edit_supplier_get),
    path('edit-supplier-post/<int:iidee>/', edit_supplier_post),
    
    # product urls
    path('products/', productlistview),
    path('add-product/',addproduct),
    path('delete-product/<int:iidee>/',deleteproduct),
    path('edit_product_get/int:iidee>/', edit_product_get),
    path('edit-product-post/<int:iidee>/', edit_product_post),
    path('products-by-supplier/<int:iidee>/', products_filtered),
]



