from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dodsbo.models import Wish
from dodsbo.models import Comment


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class VoteForm(forms.Form):
    choices = (
        (0, 'Fordel'),
        (1, 'Doner'),
        (2, 'Kast'),
    )
    choice = forms.CharField(
        label='Choice', widget=forms.RadioSelect(choices=choices))

    class Meta:
        model = Wish
        fields = ['choices']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
