from django.shortcuts import render
from .models import Person


def index(request):
    qs = Person.objects.all()
    if qs:
        ctx = {'root' : qs[0]}
    else:
        ctx = {'root' : ''}
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'edit-tree.html', context=ctx)
    return render(request, 'index.html', context=ctx)


