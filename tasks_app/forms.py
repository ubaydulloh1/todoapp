from django.forms import ModelForm
from .models import Task


class TaskModelForm(ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'
        fields = ['title', 'description']
    
    def __init__(self, *args, **kwargs):
        super(TaskModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input is-primary',})

