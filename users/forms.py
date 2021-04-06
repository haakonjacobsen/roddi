from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dodsbo.models import Wish, Alert
from dodsbo.models import Comment


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

class AlertForm(forms.Form):

    class Meta:
        model = Alert
        fields = ['estateID','user']

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
