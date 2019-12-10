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
    all_orders = Order.objects.all()
    total_quantity = 0
    total_price = 0
    for item in all_orders:
        total_quantity += item.quantity_ordered
        total_price += item.total_price
    context = {
        'orders':all_orders,
        'this_order':this_order,
        'total_quantity':total_quantity,
        'total_price':total_price
    }
    return render(request, "store/checkout.html", context)
