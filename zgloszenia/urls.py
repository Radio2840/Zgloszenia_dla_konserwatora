from django.shortcuts import redirect
from django.urls import path

from zgloszenia.views import create_report, user_login, logoutme, home_view, report_view, get_image, your_reports_view, change_report_status

urlpatterns = [
    path('', lambda request: redirect('home')),
    path('addreport/', create_report, name='addreport'),
    path('home/addreport', create_report, name='addreport'),
    path('home/', home_view, name='home'),
    path('report', report_view, name='report'),
    path('login/', user_login, name='login'),
    path('logoutme', logoutme, name="logoutme"),
    path('fotos', get_image, name='viewimg'),
    path('your_reports', your_reports_view, name='your_reports'),
    path('report/edit/status', change_report_status, name='report_edit_status'), 

]