from django.shortcuts import render, HttpResponse, redirect
from admin_app.models import RoleDetails
from django.contrib.auth.hashers import check_password


def front_index(request):
    return render(request, "front_index.html")


def sign_in(request):
    if request.method == "POST":
        email = request.POST['email']
        u_pass = request.POST['password']
        try:
            data = RoleDetails.objects.get(email=email)
            if check_password(u_pass, data.password):
                if data.is_active == 1:
                    role = data.role.role_name
                    request.session['auth'] = True
                    request.session['name'] = data.first_name
                    request.session['role'] = role
                    if role == "admin":
                        return redirect("/admin_index/")
                else:
                    return HttpResponse("please verify your email")
        except:
            return HttpResponse('data not found')
    return render(request, "sign-in.html")
