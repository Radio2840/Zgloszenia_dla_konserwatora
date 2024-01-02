from django.urls import path

from konserwator.views import login_view, home_view
from zgloszenia.views import add_report

urlpatterns = [
    path('addreport/', add_report, name='addreport'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name="home"),
]