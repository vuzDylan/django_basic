from django.shortcuts import render_to_response, HttpResponseRedirect, get_object_or_404
from django.template.context_processors import csrf
from django.core.exceptions import PermissionDenied
from todo.forms import TodoForm
from todo.models import Todo

def view_todos(request):
    args = {}
    args.update(csrf(request))
    args['user'] = request.user
    args['todos'] = Todo.objects.filter(user=request.user)
    return render_to_response('todos.html', args)

def view_completed(request):
    args = {}
    args.update(csrf(request))
    args['user'] = request.user
    args['todos'] = Todo.objects.filter(user=request.user, completed=True)
    return render_to_response('todos.html', args)

def view_uncompleted(request):
    args = {}
    args.update(csrf(request))
    args['user'] = request.user
    args['todos'] = Todo.objects.filter(user=request.user, completed=False)
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

def toggle_todo(request, post_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=post_id)
        todo.completed = not todo.completed
        todo.save()
        return HttpResponseRedirect('/todo/all')

    else:
        raise PermissionDenied
