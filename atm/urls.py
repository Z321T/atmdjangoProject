from django.urls import path
from django.contrib.staticfiles.views import serve
from .views import LoginView
from .views import Withdraw

app_name = 'atm'

urlpatterns = [

    path('static/<path:path>', serve),
    path('login/', LoginView.as_view(), name='login'),
    path('withdraw/', Withdraw.as_view(), name='withdraw')

]
