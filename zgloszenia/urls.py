from django.shortcuts import redirect
from django.urls import path

from zgloszenia.views import create_report, user_login, logoutme, home_view, report_view, get_image

urlpatterns = [
    path('', lambda request: redirect('home')),
    path('addreport/', create_report, name='addreport'),
    path('home/addreport', create_report, name='addreport'),
    path('home/', home_view, name='home'),
    path('report', report_view, name='report'),
    path('login/', user_login, name='login'),
    path('logoutme', logoutme, name="logoutme"),
    path('fotos', get_image, name='viewimg')
]