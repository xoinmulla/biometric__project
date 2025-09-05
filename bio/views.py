# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PhotoForm, RegistrationForm, LoginForm
from .models import Photo


# Home / Upload page (authenticated only)
@login_required(login_url="login")
def index(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # Optional: if you want to assign ownership of photo to the user
            # photo.user = request.user
            photo.save()
            messages.success(request, "Photo uploaded successfully!")
            return redirect("index")
    else:
        form = PhotoForm()

    photos = Photo.objects.all().order_by("-uploaded_at")
    return render(request, "index.html", {"form": form, "photos": photos})


# Registration
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Registration successful. Please login.")
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


# Login
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# Logout
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")
