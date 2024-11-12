from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


# Create your views here.
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("myapp:dashboard") # OR your success URL
    else:
        form = ProductForm()

    return render(request, "myapp/upload.html", {"form": form})


def dashboard_view(request):
    products = Product.objects.all()
    return render(request, "myapp/dashboard.html", {"products": products})

