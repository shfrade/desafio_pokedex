from django.shortcuts import render
from .models import Pokemon
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404
from django.http import Http404


# Create your views here.
def listar_todos(request):
    # todos os objetos do DB.
    pokemons_list = Pokemon.objects.all().order_by('-nome')
    # abaixo, para saber QUANTAS páginas devem aparecer
    paginator = Paginator(pokemons_list, 3)
    # abaixo, pega qual página o usuário esta
    page = request.GET.get('page')
    # abaixo, pega quais os registros são desta página
    pokemons = paginator.get_page(page)

    contexto = {
        'pokemons': pokemons
    }
    return render(request, 'listar_todos.html', contexto)


def pokemon(request, pokemon):
    pokemon_obj = get_object_or_404(Pokemon, nome__iexact=pokemon)
    # todo refazer a página 404.
    '''
    # Faz o mesmo que a linha 25 nestas linhas 28 até 31
    try:
        pokemon_obj = Pokemon.objects.get(nome__iexact=pokemon)
    except Pokemon.DoesNotExist:
        raise Http404("Não existe esse pokemon.")
    '''
    # where upper(nome) == upper(pokemon)

    contexto = {'pokemon': pokemon_obj}
    return render(request, 'pokemon.html', contexto)
