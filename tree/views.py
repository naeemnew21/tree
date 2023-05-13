from django.shortcuts import render
from .models import Person


def index(request):
    ctx = {'root' : Person.objects.all()[0]}
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'edit-tree.html', context=ctx)
    return render(request, 'index.html', context=ctx)


