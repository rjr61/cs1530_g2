from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'profile'
urlpatterns = [
    path('',  login_required(views.index, login_url='login/'), name='index'),
]