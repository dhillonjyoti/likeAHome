from django.shortcuts import render, HttpResponse, redirect
from admin_app.models import UserRole, RoleDetails
from admin_app.form import RoleDetailsForm
from django.contrib.auth.hashers import make_password
from miscFiles.verification_mail import verify_link_send
from miscFiles.generic_functions import generate_random_string
from miscFiles.authenticate import authentication
from django.contrib.auth.views import logout


def admin_signup(request):
    if request.method == "POST":
        users_role = UserRole.objects.get(role_name="admin")
        detail_form = RoleDetailsForm(request.POST)
        if detail_form.is_valid():
            form = detail_form.save(commit=False)
            form.role_id = users_role.role_id
            form.first_name = request.POST['first_name']
            form.last_name = request.POST['last_name']
            form.email = request.POST["email"]
            password = request.POST["password"]
            c_pass = request.POST["c_pass"]
            if password == c_pass:
                form.password = make_password(request.POST["password"])
            else:
                return HttpResponse("password doesn't match")
            token = make_password(generate_random_string()).replace("+", "")
            form.verify_link = token
            link = "127.0.0.1:8000/verify/?link={}".format(token)
            form.save()
            verify_link_send(request.POST["email"], request.POST['first_name'], link)
            return redirect("/")

    return render(request, 'sign-up.html')


def sign_up(request):
    if request.method == "POST":
        detail_form = RoleDetailsForm(request.POST)
        if detail_form.is_valid():
            form = detail_form.save(commit=False)
            form.role_id = int(request.POST['role'])
            form.first_name = request.POST['first_name']
            form.last_name = request.POST['last_name']
            form.email = request.POST["email"]
            password = request.POST["password"]
            c_pass = request.POST["c_pass"]
            if password == c_pass:
                form.password = make_password(request.POST["password"])
            else:
                return HttpResponse("passsword dont match")
            token = make_password(generate_random_string()).replace("+", "")
            form.verify_link = token
            link = "127.0.0.1:8000/verify/?link={}".format(token)
            form.save()
            verify_link_send(request.POST["email"], request.POST['first_name'], link)
            return redirect("/")
        else:
            return HttpResponse("Form not valid")
    users_role = UserRole.objects.all()
    data = []
    for i in users_role:
        if i.role_name != "admin":
            data.append(i)
    return render(request, 'sign-up.html', {"users_role": data})


def user_verify(request):
    get_url = request.GET['link']
    try:
        data = RoleDetails.objects.get(verify_link=get_url)
        update = RoleDetails(email=data.email, verify_link="", is_active=1)
        update.save(update_fields=['verify_link', 'is_active'])
        return redirect("/")
    except:
        return HttpResponse("invalid token")


def admin_index(request):
    try:
        auth = authentication(request.session['auth'], request.session['role'], "admin")
        if auth is True:
            return render(request, "admin_index.html")
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