from django import forms

from zgloszenia.models import Report


class LoginForm(forms.Form):
    username = forms.CharField(label='login', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'foto', 'importance_of_the_report']

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['importance_of_the_report'].widget = forms.Select(choices=Report.IMPORTANCE_CHOICES)

