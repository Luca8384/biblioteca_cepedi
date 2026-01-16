from django.urls import path
from.import views


app_name = 'autores'

urlpatterns = [

    path('', views.listar_Autores, name='listar_autores'),
    path('<int:id>/editar/', views.editar_autor, name='editar_autor'),
    path('inserir_autor/', views.inserir_autor, name='inserir_autor'),
    path('<int:id>/excluir/', views.excluir_autor, name='excluir_autor'),


]