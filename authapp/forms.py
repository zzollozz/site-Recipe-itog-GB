import random, hashlib

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth import get_user_model




class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    # def clean_age(self):
    #     current_age = self.cleaned_data['age']
    #     if current_age < 18:
    #         raise forms.ValidationError("Вы слишком молоды!")
    #     return current_age

    # def save(self):
    #     user = super(UserRegisterForm, self).save()
    #
    #     user.is_active = False
    #     salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
    #     user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
    #     user.save()
    #     return user
