from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'hello_world/base.html', context={})
