from django.shortcuts import render


def back_index(request):
    return render(request, 'back_index.html')