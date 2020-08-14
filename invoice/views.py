from django.shortcuts import render,redirect
from  invoice.forms import InvoiceForm
from  invoice.models import Invoice
from django.http import HttpResponse

# Create your views here.
def create(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("invoice:view_invoice")
            except:
                return HttpResponse(form.errors)
    else:
        form = InvoiceForm()
    return render(request, "Invoice/createinvoice.html", {'form': form})

def display(request):
    invoice = Invoice.objects.all()
    return render(request,"Invoice/showinvoice.html", {'invoice': invoice})