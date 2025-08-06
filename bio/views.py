from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def index(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PhotoForm()
    photos = Photo.objects.all().order_by('-bio')
    return render(request, 'index.html', {'form': form, 'photos': photos})
