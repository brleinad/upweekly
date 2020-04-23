from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
#        self.fields['password1'].help_text = '''
#Your password can’t be too similar to your other personal information.
#Your password must contain at least 8 characters.
#Your password can’t be a commonly used password.
#Your password can’t be entirely numeric.
#'''
        self.fields['password1'].help_text = 'Must contain at least 8 characters'
        self.fields['password2'].help_text = ''

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2',)
        #help_texts['password1'] = 'BOB'
        help_texts = {
                'password1': 'BOB',
                }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)
