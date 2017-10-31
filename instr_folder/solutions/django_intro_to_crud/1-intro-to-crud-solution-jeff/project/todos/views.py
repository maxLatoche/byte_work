from django.shortcuts import render, redirect
from todos.models import Todo


def index(request):
    todos = Todo.objects.filter(deleted=False)
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


def create(request):
    if request.method == "POST":
        # handle the form data
        todo_string = request.POST['task']

        todo = Todo(task=todo_string)

        todo.save()

        return redirect('todos:index')

    elif request.method == "GET":
        return render(request, 'todos/create.html')


def read(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    if todo.deleted == True:
        return redirect('todos:index')
        
    context = {
        'todo': todo
    }
    return render(request, 'todos/read.html', context)


def update(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)

        if todo.task != request.POST['task']:
            todo.task = request.POST['task']
            todo.save()

        return redirect('todos:index')


def delete(request, todo_id):
    
    todo = Todo.objects.get(id=todo_id)

    todo.jeff_delete()

    return redirect('todos:index')
