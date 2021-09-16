from django.http.response import HttpResponse, HttpResponseNotFound
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
#Изменение данных из БЛД
def edit(request, id):
    try:
        todo = ToDo.objects.get(id = id)
        if request.method == 'POST':
            todo.title = request.POST.get("title")
            todo.description = request.POST.get("description")
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html',{'todo':todo})
    except ToDo.DoesNotExist:
        return HttpResponseNotFound('<h2>Задачка не найдена</h2>')

#Удаления данных из БЛД
def delete(request, id):
    try:
        todo = ToDo.objects.get(id = id)
        todo.delete()
        return HttpResponseRedirect('/')
    except ToDo.DoesNotExist:
        return HttpResponseNotFound('<h2>Задачка не найдена</h2>')