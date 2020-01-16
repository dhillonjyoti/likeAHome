from django.shortcuts import render
from front_app.models import UserRole
from django.contrib.auth.models import User


def back_index(request):
    return render(request, 'back_index.html')


def sign_in(request):
    if request.method == "POST":
        pass
    return render(request, 'sign-in.html')


def sign_up(request):
    users_role = UserRole.objects.all()
    data = users_role[1:]
    return render(request, 'sign-up.html', {"users_role": data})