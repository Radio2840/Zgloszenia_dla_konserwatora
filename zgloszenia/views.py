from django.shortcuts import render, redirect

from zgloszenia.forms import ReportForm


def add_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.autor = request.user
            report.save()
            return redirect('listOfReports')
    else:
        form = ReportForm()

    return render(request, 'addReport.html', {'form': form})
