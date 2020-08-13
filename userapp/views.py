from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required
def index(request):
    return render(request,"index.html")

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("login")
            except:
                return HttpResponse(form.errors)
        else:
            return render(response , "user/signup.html", {"form":form})
    else:
        form = RegisterForm()
    return render(response , "user/signup.html", {"form":form})

