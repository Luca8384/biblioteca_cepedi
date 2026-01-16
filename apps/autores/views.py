from django.contrib import messages

from .forms import AutorForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor



def inserir_autor(request):
    template_name = 'autores/form_autor.html'
    if request.method == 'POST':
        form = AutorForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro do Autor foi realizado com sucesso!')
        return redirect('autores:listar_autores')
    form = AutorForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_Autores(request):
    template_name = 'autores/listar_autores.html'
    autores = Autor.objects.all()
    context = {'relacao_autores': autores}
    return render(request, template_name, context)

def editar_autor(request, id):
    template_name = 'autores/form_autor.html'
    autor = get_object_or_404(Autor, id=id)
    form = AutorForm(request.POST or None, request.FILES or None, instance=autor)
    context = {'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
        return redirect('autores:listar_autores')
    return render(request, template_name, context)


def excluir_autor(request, id):
    template_name = 'autores/excluir_autor.html'
    autor = Autor.objects.get(id=id)
    context = {'autor': autor}
    if request.method == "POST":
        autor.delete()
        messages.error(request, 'O autor foi excluída com sucesso.')
        return redirect('autores:listar_autores')
    return render(request, template_name, context)


def detalhe_livro(request, id):
    autor = get_object_or_404(Autor, id=id)
    return render(request, 'autores/detalhe_autor.html', {'autor': autor})
from django.shortcuts import render

# Create your views here.
