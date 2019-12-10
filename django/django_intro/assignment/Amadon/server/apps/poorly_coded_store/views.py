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
    request.session['total_char']=total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    request.session['this_order'] = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    request.session['all_order'] = Order.objects.all()
    total_quantity = 0
    total_price = 0
    for item in all_orders:
        total_quantity += item.quantity_ordered
        total_price += item.total_price
    request.session['total_quantity']
    request.session['total_price']
    return redirect('/amadon/checkout/thankyou')

def thankyou(request, context):
    return render(request, 'store/checkout.html', context)
