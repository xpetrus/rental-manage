from django.urls import include, path
from django.conf.urls import url
from . import views

app_name = 'rentals'
urlpatterns = [
    path('', views.rental_detail_view, name='index'),
    path('vendor/', views.vendor_detail_view, name='vendor'),
    path('invoice/', views.invoice_detail_view, name='invoice'),
    ]