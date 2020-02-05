from django.shortcuts import render, HttpResponse, redirect
from miscFiles.authenticate import authentication
from django.contrib.auth.views import logout

def pg_index(request):
    try:
        auth = authentication(request.session['auth'], request.session['role'], "pg")
        if auth is True:
            return render(request, "pg_index.html")
        else:
            status, msg = auth
            if msg == "invalid_user":
                return HttpResponse("invalid user")
            elif msg == "not_login":
                return redirect("/")
    except:
        return redirect("/")


def user_logout(request):
    logout(request)
    return redirect("/sign_in/")