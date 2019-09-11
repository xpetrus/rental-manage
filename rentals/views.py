from django.shortcuts import render, redirect, get_object_or_404
from .models import Rental, Vendor, Invoice
from .forms import RentalForm


# Create your views here.
def rental_detail_view(request):
    obj = Rental.objects.all()
    context = {
        'rentals': obj
    }
    return render(request, 'rentals/index.html', context)


def rental_details(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    return render(request, 'rentals/rental_details.html', {'rental': rental})


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


def new_rental(request):
    if request.method == "POST":
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.save()
            return redirect('rentals:rental_details', pk=rental.pk)  # rentals:specify applicatiionlevel
        else:
            return render(request, 'rentals/add_rental.html', {'form': form})
    else:
        form = RentalForm()
        return render(request, 'rentals/add_rental.html', {'form': form})
