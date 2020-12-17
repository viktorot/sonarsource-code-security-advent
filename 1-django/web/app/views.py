from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    return HttpResponse(render(request, 'index.html', context))