from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from .models import ToDo


# Create your views here.
def homepage(request):
    todos = ToDo.objects.all()
    return render(request, "index.html", {'todos': todos})

def create (request):
    if request.method == 'POST':
        todo=ToDo()
        todo.title=request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
    return HttpResponseRedirect('/')
