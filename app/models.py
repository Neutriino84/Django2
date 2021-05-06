from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default = 'lakufirma')
    contactname = models.CharField(max_length = 50, default = 'Tommi')
    address = models.CharField(max_length = 100, default = 'tie 3')
    phone = models.CharField(max_length = 20, default = '0700123123')
    email = models.CharField(max_length = 50, default = 'mika.silli@silli.com')
    country = models.CharField(max_length = 50, default = 'lakufirma')

class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "laku")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.IntegerField(default = 3)
    unitsinstock = models.IntegerField(default = 3)
    companyname = models.CharField(max_length = 50, default = 'lakufirma')