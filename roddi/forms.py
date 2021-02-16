from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Bekreft passord', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('User name',)

    def clean_username(self):
        user_name = self.cleaned_data('User name')
        qs = User.objects.filter(user_name=user_name)
        if qs.exists():
            raise forms.ValidationError("brukernavnet er tatt")
        return user_name

    def clean_password2(self):
        # metode for å sjekke at de to passordene matcher
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passordene samsvarer ikke")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """
    Django har en Form classe som brukes til å lage HTML forms
    """
    password1 = forms.CharField(label='Passord', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Passord bekreftelse', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('User name',)

    def clean_password2(self):
        # sjekker om passordene er like
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passordene samsvarer ikke")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """
    En form for å oppdatere brukere
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('User name', 'password', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
