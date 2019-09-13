from django.urls import include, path
from django.conf.urls import url
from . import views

app_name = 'rentals'
urlpatterns = [
    path('', views.rental_detail_view, name='index'),
    url(r'^rental/(?P<pk>\d+)$', views.rental_details, name='rental_details'),
    url(r'^vendor/(?P<pk>\d+)$', views.vendor_details, name='vendor_details'),
    url(r'^invoice/(?P<pk>\d+)$', views.invoice_details, name='invoice_details'),
    path('vendor/', views.vendor_detail_view, name='vendor'),
    path('invoice/', views.invoice_detail_view, name='invoice'),
    url(r'^rental/new/$', views.new_rental, name='new_rental'),
    url(r'^vendor/new/$', views.new_vendor, name='new_vendor'),
    url(r'^invoice/new/$', views.new_invoice, name='new_invoice'),
    url(r'^vendor/filter_vendor/$', views.filter_vendor, name='filter_vendor'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.del_vendor, name='del_vendor'),
    path('post/<int:pk>/edit/', views.vendor_edit, name='vendor_edit'),

    ]