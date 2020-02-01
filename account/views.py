from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm,UserProfileForm
from .models import UserProfile

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    # Redirect to profile
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    profile_form = UserProfileForm(request.POST or None)
    if form.is_valid() and profile_form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        profile  = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
        'profile_form':profile_form
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


# @login_required
def home(request):
    user = request.user
    return render(request, "home.html", {'user':user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        instance = UserProfile.objects.filter(user=request.user)
        if not instance:
            instance = UserProfile.objects.create(user=request.user)
        else:
            instance = instance.first()
        profile_form = UserProfileForm(data = request.POST or None , instance=instance)#,files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
    else:
        instance = UserProfile.objects.filter(user=request.user)
        if not instance:
            instance = UserProfile.objects.create(user=request.user)
        else:
            instance = instance.first()
        profile_form = UserProfileForm(instance=instance)
    
    context = {
        'profile_form':profile_form
    }
    return render(request, 'edit-profile.html',context)