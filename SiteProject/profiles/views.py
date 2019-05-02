from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile, Group

# Create your views here.

def index(request):
    return render(
        request,
        'profiles/index.html',
    )



