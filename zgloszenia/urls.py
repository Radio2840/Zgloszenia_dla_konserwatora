from django.urls import path

from zgloszenia.views import home_view, create_report, user_login, logoutme

urlpatterns = [
    path('addreport/', create_report, name='addreport'),
    path('home/', home_view, name='home'),
    path('login/', user_login, name='login'),
    path('logoutme', logoutme, name="logoutme"),
]