from django.shortcuts import render

# Shop page
def product_list(request):
    return render(request, "product_list.html")

# Cart page
def cart_page(request):
    return render(request, "cart.html")
from django.shortcuts import render

def shop(request):
    return render(request,'home.html')