from django.shortcuts import render
from django.http import HttpResponse

def shop_index(request):
    print("Shop page loaded")  
    return render(request, 'shop/index.html')