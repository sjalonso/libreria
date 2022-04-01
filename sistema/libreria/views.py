from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

def inicio(request):
   return render(request, ('paginas/home.html'))  

def nosotros(request):
    return render(request, ('paginas/nosotros.html'))    

#funciones de acceso a libro
def libros(request):
    libros = Libro.objects.all()
    return render(request, ('libros/index.html'), {'libros': libros})   

def new_libro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/new.html', {'formulario': formulario}) 

def edit_libro(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')

    return render(request, 'libros/edit.html', {'formulario': formulario})


def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

# Create your views here.
