from django.shortcuts import render, render_to_response
from .forms import RegisterForm
from .models import Users
from django.contrib.auth import authenticate, logout

def index(requet):
    return render_to_response('base.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST['Username']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        trole = request.POST['Role']
        users = [i[0] for i in list(Users.objects.all().values_list('username'))]
        if username in users:
            uname_message = '该用户名已存在'
            return render_to_response("signup.html", locals())
        if password1 == password2:
            user = User.objects.create_user(username, password=password1, role=trole)
            user.save()
            # inituser(username)
            request.session['username'] = username
            return render_to_response('index.html', locals())
        else:
            psw_message = '两次输入的密码不同'
            render_to_response("signup.html", locals())
    else:
        return render_to_response("signup.html", locals())


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            request.session.set_expiry(0)
            user = Users.objects.get(username=username)
            return render_to_response("index.html", locals())
        else:
            message = '用户不存在或密码错误'
            return render_to_response("login.html", locals())
    else:
        return render_to_response("login.html", locals())