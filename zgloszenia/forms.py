from django import forms
from .models import Report

# Login form for users


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Form for adding reports to the database by employees and conservators


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'foto', 'importance_of_the_report']

    title = forms.CharField(label='Tytuł', max_length=150, required=True)
    description = forms.CharField(label='Opis', widget=forms.Textarea(attrs={'rows': 3}), max_length=250, required=True)
    foto = forms.ImageField(label='Zdjęcie', required=False)
    importance_of_the_report = forms.ChoiceField(label='Ważność', choices=Report.IMPORTANCE_CHOICES, initial=1, widget=forms.Select(attrs={'class': 'form-control'}))


