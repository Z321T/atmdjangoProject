from django.urls import path
from django.contrib.staticfiles.views import serve
from .views import login

app_name = 'atm'

urlpatterns = [

    path('static/<path:path>', serve),
    path('login/', login, name='login'),

]
