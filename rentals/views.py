from django.shortcuts import render
from .models import Rental, Vendor, Invoice


# Create your views here.
def rental_detail_view(request):
    obj = Rental.objects.all()
    context = {
        'rentals': obj
    }
    return render(request, 'rentals/index.html', context)


def vendor_detail_view(request):
    obj = Vendor.objects.all()
    context = {
        'vendors': obj
    }
    return render(request, 'rentals/vendortab.html', context)


def invoice_detail_view(request):
    obj = Invoice.objects.all()
    context = {
        'invoices': obj
    }
    return render(request, 'rentals/invoicetab.html', context)


