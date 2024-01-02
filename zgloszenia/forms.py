from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as lazy
from .models import CustomUser, Report


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label="Hasło",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Login'

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'foto', 'importance_of_the_report']

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Tytuł zgłoszenia'
        self.fields['description'].label = 'Opis zgłoszenia'
        self.fields['foto'].label = 'Załącz zdjęcie (opcjonalne)'
        self.fields['importance_of_the_report'].label = 'Ważność zgłoszenia'
        self.fields['title'].required = True
        self.fields['description'].required = True
        self.fields['importance_of_the_report'].required = True
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 4})

    def clean_foto(self):
        foto = self.cleaned_data['foto']

        if not foto:
            return None

        return foto


