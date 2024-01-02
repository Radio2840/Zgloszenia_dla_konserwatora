from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from zgloszenia.forms import LoginForm, ReportForm


def login_view(request):
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                if user.role == 'Konserwator':
                    return redirect('home_view')
                elif user.role == 'school_employee':
                    return redirect('home')
                else:
                    return redirect('home')
            else:
                error_message = 'Invalid username or password.'
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error_message': error_message})


def add_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.notifier = request.user
            report.save()
            return redirect('success_page')
    else:
        form = ReportForm()

    return render(request, 'zglaszajacy/addreport.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')