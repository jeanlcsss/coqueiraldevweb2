# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

# Listar produtos
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'products/listar_produtos.html', {'produtos': produtos})

# Detalhes do produto
def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'products/detalhes_produto.html', {'produto': produto})

# Criar produto
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'products/criar_editar_produto.html', {'form': form})

# Editar produto
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('products:listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'products/criar_editar_produto.html', {'form': form})

# Excluir produto
def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('products:listar_produtos')
    return render(request, 'products/excluir_produto.html', {'produto': produto})
