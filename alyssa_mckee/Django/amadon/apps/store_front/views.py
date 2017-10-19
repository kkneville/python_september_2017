from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, "store_front/index.html")
def process(req):
	items_prices = {
		"shirt":19.99,
		"sweater":29.99,
		"duck":4.99,
		"book":49.99		
	}
	if not 'total' in req.session:
		req.session['total'] = 0
	if not 'itemcount' in req.session:
		req.session['itemcount'] = 0
	
	price = items_prices[req.POST['item']]
	
	req.session['price'] = price*float(req.POST['quantity'])
	req.session['total'] = req.session['total'] + price*float(req.POST['quantity'])
	print(req.session['total'])
	req.session['itemcount'] += 1*int(req.POST['quantity'])
	
	
	return redirect("/amadon/checkout")
def checkout(req):
	return render(req, "store_front/checkout.html")