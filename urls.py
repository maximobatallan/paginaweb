
from django.urls import path

from lynx import views

urlpatterns = [

    # - Homepage

    path('', views.home, name=""),
    path('registrarcurso/', views.registrarCurso)


]









