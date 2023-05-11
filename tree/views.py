from django.shortcuts import render
from .models import Person


def index(request):
    ctx = {'root' : Person.objects.all()[0]}
    return render(request, 'index.html', context=ctx)