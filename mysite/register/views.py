# redirect is to send new users someplace after reg
from django.shortcuts import render, redirect
# Reference the RegisterForm class we defined in forms.py
from .forms import RegisterForm

# Create your views here.

# Use the built-in form imported above for user creation
def register(response):
    # can use is_valid method because built-in form
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else: 
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})