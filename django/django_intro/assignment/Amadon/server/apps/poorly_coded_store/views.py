from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    this_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    context = {
        'orders':Order.objects.all(),
        'this_order':this_order
    }
    return render(request, "store/checkout.html", context)
