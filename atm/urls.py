from django.urls import path
from django.contrib.staticfiles.views import serve

app_name = 'atm'

urlpatterns = [

    path('static/<path:path>', serve),

]
