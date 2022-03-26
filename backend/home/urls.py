
from django.urls import re_path
from django.urls import path
from home.views import test_home, test_home_api

urlpatterns = [
    path('api/', test_home_api, name='test_home_api'),
    path('', test_home,name='test_home')
]