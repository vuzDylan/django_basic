from django.shortcuts import render_to_response
from todo.models import Todo

def view_todos(request):
    args = {}
    args['user'] = request.user
    args['todos'] = Todo.objects.filter(user=request.user)
    return render_to_response('todos.html', args)


