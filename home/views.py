from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'text': 'Olá home'
    }

    return render(request, 'home/index.html', context,)

