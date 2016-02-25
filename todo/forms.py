from todo.models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'details']

    def __init__(self, *args, **kwargs):
        # super will init all the fields
        super(TodoForm, self).__init__(*args, **kwargs)
        # loop though all of the fields (order dic so you must use .items() in python3)
        for name, field in self.fields.items():
            # check if we have alread assign classes to a field above
            if "class" in field.widget.attrs:
                # the space is very important because of the way this works
                # if you dont belive me or want to see for your self try removing it
                field.widget.attrs['class'] += " form-control"
            # prop the one that will be called most often
            else:
                field.widget.attrs['class'] = "form-control"
            field.widget.attrs['placeholder'] = name
