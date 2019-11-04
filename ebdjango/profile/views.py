from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm

# from .models import User

def index(request):
    return render(request, 'profile/index.html')