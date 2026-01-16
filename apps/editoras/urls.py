from django.urls import path
from.import views


app_name = 'editoras'

urlpatterns = [

    path('listar_editoras/', views.listar_Editoras, name='listar_editoras'),
    path('<int:id>/editar/', views.editar_editora, name='editar_editora'),
    path('inserir_editora/', views.inserir_editora, name='inserir_editora'),
    path('<int:id>/excluir/', views.excluir_editora, name='excluir_editora'),


]