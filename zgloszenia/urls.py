from django.urls import path

from zgloszenia.views import home_view_k, create_report, user_login, logoutme, home_view_p

urlpatterns = [
    path('addreport/', create_report, name='addreport'),
    path('homep/addreport', create_report, name='addreport'),
    path('homek/', home_view_k, name='homek'),
    path('homep/', home_view_p, name='homep'),
    path('login/', user_login, name='login'),
    path('logoutme', logoutme, name="logoutme"),
]