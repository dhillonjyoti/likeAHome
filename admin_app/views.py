from django.shortcuts import render


def back_index(request):
    return render(request, 'back_index.html')

def sign_in(request):
    return render(request, 'sign-in.html')
