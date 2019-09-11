from django.urls import include, path
from django.conf.urls import url
from . import views

app_name = 'rentals'
urlpatterns = [
    path('', views.rental_detail_view, name='index'),
    url(r'^rental/(?P<pk>\d+)$', views.rental_details, name='rental_details'),
    path('vendor/', views.vendor_detail_view, name='vendor'),
    path('invoice/', views.invoice_detail_view, name='invoice'),
    url(r'^rental/new/$', views.new_rental, name='new_rental'),
    # url(r'^rental/new/$', views.new_rental, name='new_rental'),
    # url(r'^rental/new/$', views.new_rental, name='new_rental'),

    ]