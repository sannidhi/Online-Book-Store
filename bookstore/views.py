# Create your views here.

from models import Product
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_cart import Cart
from django_cart.cart import ItemAlreadyExists, ItemDoesNotExist


def index(request):
    object_list = Product.objects.all()
    book_listing = []
    for object in object_list:
        book_dict = {}
        book_dict['id'] = object.Productid
        book_dict['title'] = object.title
        book_dict['author'] = object.author
        book_dict['url'] = object.get_absolute_url
        book_listing.append(book_dict)
    return render_to_response('bookstore/product_list.html',{'book_listing' : book_listing})

def product(request,product_id):
    product = Product.objects.get(Productid=product_id)
    #return HttpResponse("You're voting on poll %s." % product_id)
    return render_to_response('bookstore/product_details.html',{'product' : product})

def add_to_cart(request, product_id):
	product = Product.objects.get(Productid=product_id)
	cart = Cart(request)
	try:
		quantity = int(request.POST['quantity']) or 1
		cart.add(product, product.price, quantity)
	except ItemAlreadyExists:
		pass
	return HttpResponseRedirect('/bookstore/cart/view')

def remove_from_cart(request, product_id):
	product = Product.objects.get(Productid=product_id)
	cart = Cart(request)
	try:
		cart.remove(product)
	except ItemDoesNotExist:
		pass
	return HttpResponseRedirect('/bookstore/cart/view')

def get_cart(request):
	return render_to_response('bookstore/cart.html', dict(cart=Cart(request)))

def clear_cart(request):
	cart = Cart(request)
	try:
		cart.clear()
	except Exception, exc:
		pass
	return render_to_response('bookstore/cart.html', dict(cart=cart))
