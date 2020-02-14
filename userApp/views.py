from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.


def user_register_page(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f'account created successfuly for {username}')
            return redirect("mainApp:mainpage")
    else:
        form = UserRegisterForm()
    return render(request, 'userApp/userRegisterPage.html', {"form": form})


def profile_page(requesr):
    pass
