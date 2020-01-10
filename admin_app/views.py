from django.shortcuts import render
from django.contrib.auth.models import User


def back_index(request):
    return render(request, 'back_index.html')


def sign_in(request):
    if request.method == "POST":
        pass
    return render(request, 'sign-in.html')
