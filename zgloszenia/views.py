from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from zgloszenia.forms import ReportForm, LoginForm
from zgloszenia.models import Report


def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('konto zablokowane')
            else:
                return HttpResponse('Niepoprawne dane logowania')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def create_report(request):

    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReportForm()

    return render(request, 'addreport.html', {'form': form})


@login_required
def home_view(request):
    if request.user.groups.filter(name='Konserwatorzy').exists():
        reports_done = Report.objects.filter(status_of_the_report='done').order_by('-importance_of_the_report')
        reports_not_done = Report.objects.filter(status_of_the_report='not_done').order_by('-importance_of_the_report')
        reports_in_progress = Report.objects.filter(status_of_the_report='in_progress').order_by('-importance_of_the_report')

        context = {
            'done_reports': reports_done,
            'not_done_reports': reports_not_done,
            'in_progress_reports': reports_in_progress
        }
        return render(request, 'conservators/home.html', context)
    elif request.user.groups.filter(name='Pracownicy').exists():
        return render(request, 'employees/home.html', {'home': 'home'})
    else:
        return HttpResponse("nie nalerzysz do żadnej grupy")

@login_required
def logoutme(request):

    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return render(request, 'login')


