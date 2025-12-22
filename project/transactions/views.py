from django.shortcuts import render
from transactions.models import Transaction

def cart_view(request):
    return render(request, 'transactions/cart.html')

def checkout_view(request):
    return render(request, 'transactions/checkout.html')

