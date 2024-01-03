from django import forms
from .models import Report


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'foto', 'status_of_the_report', 'importance_of_the_report']

    title = forms.CharField(label='Tytuł', max_length=150, required=True)
    description = forms.CharField(label='Opis', widget=forms.Textarea(attrs={'rows': 3}), max_length=250,
                                  required=True)
    foto = forms.ImageField(label='Zdjęcie', required=False)
    status_of_the_report = forms.ChoiceField(label='Status', choices=Report.STATUS_CHOICES, initial='not_done')
    importance_of_the_report = forms.ChoiceField(label='Ważność', choices=Report.IMPORTANCE_CHOICES, initial=1,
                                                 widget=forms.Select(attrs={'class': 'form-control'}))


