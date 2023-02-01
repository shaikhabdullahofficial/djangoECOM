from django.shortcuts import render


def layout(request):
    return render(request,"adminPages/Layout.html")


def addproduct(request):
    return render(request,"adminPages/product.html")
    
    