from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render(request,"index.html")

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = RegisterForm()
        return render(response, "user/signup.html", {"form":form})