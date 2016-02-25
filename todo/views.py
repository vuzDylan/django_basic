from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from todo.forms import TodoForm
from todo.models import Todo

def view_todos(request):
    args = {}
    args['user'] = request.user
    args['todos'] = Todo.objects.filter(user=request.user)
    return render_to_response('todos.html', args)

def create_todo(request):
    args = {}
    args.update(csrf(request))
    args['user'] = request.user
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return HttpResponseRedirect('/todo/all')
    else:
        form = TodoForm()
    args['form'] = form
    return render_to_response('create_todo.html', args)



