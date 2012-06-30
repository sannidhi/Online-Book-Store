from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView
from bookstore.models import Product


urlpatterns = patterns('',
    url(r'^$',
		ListView.as_view(
			queryset=Product.objects.all(),
			context_object_name='book_listing',
			template_name='bookstore/product_list.html')),
	url(r'^(?P<pk>\d+)/$',
		DetailView.as_view(
			model=Product,
			template_name='bookstore/product_details.html')),
	url(r'^cart/add/(?P<product_id>\d+)/$', 'bookstore.views.add_to_cart'),
	url(r'^cart/remove/(?P<product_id>\d+)/$', 'bookstore.views.remove_from_cart'),
	url(r'^cart/view$', 'bookstore.views.get_cart'),
	url(r'^cart/clear$', 'bookstore.views.clear_cart'),
)
