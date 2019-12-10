from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    request.session['purchase'] = items[request.POST['product_id']] * int(request.POST['quantity'])

    # initialization
	if 'item_count' not in request.session:
        request.session['item_count'] = 0
	if 'total_spent' not in request.session:
        request.session['total_spent'] = 0

	request.session['item_count'] += int(request.POST['quantity'])
	request.session['total_spent'] += float(request.session['purchase'])
	return redirect('/thankyou')

def thankyou(request, context):
    return render(request, 'store/checkout.html')
