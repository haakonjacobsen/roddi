from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dodsbo.models import Comment


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'name')

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
