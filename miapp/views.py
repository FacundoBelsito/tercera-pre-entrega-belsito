from django.shortcuts import render, redirect
from .forms import AutorForm, EditorialForm, LibroForm

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})

def crear_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EditorialForm()
    return render(request, 'crear_editorial.html', {'form': form})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})

def inicio(request):
    return render(request, 'index.html')
