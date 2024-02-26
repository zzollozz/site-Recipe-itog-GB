import random, hashlib

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import HiddenInput, ModelForm, TextInput, Textarea, PasswordInput
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




class UserEditForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = PasswordInput(attrs={'class': 'form-control'})
