from .forms import (UserRegisterForm,
                    ProfileUpdateForm,
                    UserUpdateForm,
                    PasswordChangeForm
                    )
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_register_page(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f'account created successfuly for {username}')
            return redirect("userApp:userLoginPage")
    else:
        form = UserRegisterForm()
    return render(request, 'userApp/userRegisterPage.html', {"form": form})


@login_required
def profile_page(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'userApp/userProfilePage.html', {"u": request.user, "user": user})


@login_required
def update_profile_page(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('userApp:userProfilePage')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'userApp/profileUpdatePage.html', context)


@login_required
def delete_profile_page(request, username):
    u = User.objects.get(username=username)
    if request.method == 'POST':
        u.delete()
        messages.success(request, 'Your account has been updated!')
        return redirect('mainApp:mainpage')
    else:
        return render(request, 'userApp/userDeleteProfile.html')

    return render(request, 'userApp/userDeleteProfile.html')


@login_required
def password_change_page(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been Changed!')
            return redirect('userApp:userProfilePage')
        else:
            messages.error(request, 'Form wasnot VALID')
            return redirect('userApp:changePasswordPage')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'userApp/passwordChangePage.html', {"form": form})
