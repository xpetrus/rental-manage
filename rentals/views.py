from django.shortcuts import render, redirect, get_object_or_404
from .models import Rental, Vendor, Invoice
from .forms import RentalForm, VendorForm, InvoiceForm


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


def vendor_details(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(request, 'rentals/vendor_details.html', {'vendor': vendor})


def invoice_detail_view(request):
    obj = Invoice.objects.all()
    context = {
        'invoices': obj
    }
    return render(request, 'rentals/invoicetab.html', context)


def invoice_details(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'rentals/invoice_details.html', {'invoice': invoice})


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


def new_invoice(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.save()
            return redirect('rentals:invoice_details', pk=invoice.pk)  # rentals:specify applicatiionlevel
        else:
            return render(request, 'rentals/add_invoice.html', {'form': form})
    else:
        form = InvoiceForm()
        return render(request, 'rentals/add_invoice.html', {'form': form})


def new_vendor(request):
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.save()
            return redirect('rentals:vendor_details', pk=vendor.pk)  # rentals:specify applicatiionlevel
        else:
            return render(request, 'rentals/add_vendor.html', {'form': form})
    else:
        form = VendorForm()
        return render(request, 'rentals/add_vendor.html', {'form': form})


def filter_vendor(request):
    query = request.GET.get('salesperson')
    if query:
        results = Vendor.objects.filter(Sales_Person=query)
        context = {
            'vendors': results
        }
        return render(request, 'rentals/vendortab.html', context)


