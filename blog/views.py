from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    context = {
        'text': 'Ola Blog',
        'tittle': 'Pagina Exemplo - ',
    }
    return render(request, 'blog/index.html', context)