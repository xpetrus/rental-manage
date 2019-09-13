from .models import Rental, Vendor, Invoice
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ('Job_ID', 'Equipment_Needed_from', 'Equipment_Needed_Until', 'PO_Num', 'Receive_Date', 'Buy_or_Rent',
                  'Return_Date', 'Receive_Hour', 'Return_Hour', 'Rental_Rate', 'Enter_Equipment_ID', 'Category',
                  'Make', 'Model', 'Serial_Number')
        widgets = {
            'Equipment_Needed_from': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'Equipment_Needed_Until': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'Receive_Date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'Return_Date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'Receive_Hour': forms.TimeInput(attrs={'placeholder': 'Hour:Minutes'}),
            'Return_Hour': forms.TimeInput(attrs={'placeholder': 'Hour:Minutes'}),
        }


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('Vendor_ID', 'Sales_Person', 'Address', 'Contact')
        widgets = {
            'Contact': forms.TextInput(attrs={'placeholder': 'Phone or Email'}),
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('Job_No', 'Invoice_Date', 'Invoice_No', 'Invoice_Amount')
        widgets = {
            'Invoice_Date':forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
