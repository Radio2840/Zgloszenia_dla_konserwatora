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
                    if request.user.groups.filter(name='Konserwatorzy').exists():
                        return redirect('homek')
                    if request.user.groups.filter(name='Pracownicy').exists():
                        return redirect('homep')
                    else:
                        return HttpResponse("nie nalerzysz do żadnej grupy")
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
            return redirect('homep')
    else:
        form = ReportForm()

    return render(request, 'addreport.html', {'form': form})


@login_required
def not_done_reports(request):
    not_done_reports = Report.objects.filter(status_of_the_report='not_done')
    not_done_reports = not_done_reports.order_by('-importance_of_the_report')
    in_progres_reports = Report.objects.filter(status_of_the_report='in_progress')
    in_progres_reports = in_progres_reports.order_by('-importance_of_the_report')
    done_reports = Report.objects.filter(status_of_the_report='done')
    done_reports = done_reports.order_by('-importance_of_the_report')
    context = {'not_done_reports': not_done_reports, 'in_progress_reports': in_progres_reports, 'done_reports':done_reports}
    return render(request, 'konserwator/home.html', context)


@login_required
def logoutme(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return render(request, 'login')


@login_required
def home_view_k(request):
    return render(request, 'konserwator/home.html', {'home': 'home'})


@login_required
def home_view_p(request):
    return render(request, 'pracownicy/home.html', {'home': 'home'})