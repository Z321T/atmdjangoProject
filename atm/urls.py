from django.urls import path
from django.contrib.staticfiles.views import serve
from .views import LoginView, WithdrawView

app_name = 'atm'

urlpatterns = [

    path('static/<path:path>', serve),
    path('login/', LoginView.as_view(), name='login'),
    path('withdraw/', WithdrawView.as_view(), name='withdraw')

]
