from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic

# from .models import User

def profile(request):
    return render(request, 'profile/profile-index.html')