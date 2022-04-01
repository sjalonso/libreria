from django.urls import path
from .import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns= [
    path('inicio', views.inicio, name='inicio' ),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/newlibro', views.new_libro, name='newlibro'),
    path('libros/editlibro/<int:id>', views.edit_libro, name='editlibro'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
