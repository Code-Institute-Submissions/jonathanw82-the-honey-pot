from django.shortcuts import render


def index(request):
    """ A view to display the index page """
    return render(request, 'home/index.html')


def about(request):
    """ A view to display the about page """
    return render(request, 'home/about.html')
