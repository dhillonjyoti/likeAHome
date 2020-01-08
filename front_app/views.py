from django.shortcuts import render


def front_index(request):
    return render(request, "front_index.html")
