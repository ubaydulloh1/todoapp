from django.forms import ModelForm
from django.contrib.auth.models import User


class UserModelForm(ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input is-primary',})
            if name=='password':
                field.widget.attrs.update({'class': 'input is-primary', 'type': 'password'})
