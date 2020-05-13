from django.shortcuts import render

def index(request):
    context = {'menu_class': 'menu-container'}
    return render(request, 'home/index.html', context)
    