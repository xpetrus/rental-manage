from django.db import models

br_choice = (('buy','BUY'),('rent','RENT'))


# Create your models here.
class Rental(models.Model):
    # job info
    Job_ID = models.IntegerField(null=True)
    Equipment_Needed_from = models.DateField()
    Equipment_Needed_Until = models.DateField()
    PO_Num = models.IntegerField(null=True)
    # enter rental info
    Receive_Date = models.DateField()
    Buy_or_Rent = models.CharField(max_length=8, choices=br_choice, default='rent')
    Return_Date = models.DateField()

    Receive_Hour = models.TimeField(null=True)
    Return_Hour = models.TimeField(null=True)

    Rental_Rate = models.CharField(max_length=50)
    # Enter equipment info
    Enter_Equipment_ID = models.IntegerField(null=True)
    Category = models.CharField(max_length=50)
    Make = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Serial_Number = models.IntegerField(null=True)


class Vendor(models.Model):
    Vendor_ID = models.IntegerField(null=True)
    Sales_Person = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    Contact = models.CharField(max_length=10)


class Invoice(models.Model):
    Job_No = models.IntegerField(null=True)
    Invoice_Date = models.DateField()
    Invoice_No = models.IntegerField(null=True)
    Invoice_Amount = models.DecimalField(max_digits=25,decimal_places=2)
