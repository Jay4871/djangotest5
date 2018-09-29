from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse


# Create your views here.

# 装饰器
def check_login(func):
    def inner(request, *args, **kwargs):
        result = request.get_signed_cookie("is_login", default='0', salt='helloworld')
        if result == '1':
            return func(request, *args, **kwargs)
        else:
            next_url = request.path_info
            return redirect('/login/?next={}'.format(next_url))

    return inner


def login(request):
    print(request.get_full_path())
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.GET.get('next')
        if username == 'zhangsan' and password == '123456':
            if next_url:
                rep = redirect(next_url)
            else:
                rep = redirect('/home/')
            # rep.set_cookie("is_login",'1',max_age=10)
            rep.set_signed_cookie('is_login', '1', salt='helloworld')
            return rep

    return render(request, 'login.html')


@check_login
def home(request):
    # result=request.get_signed_cookie('is_login',0,salt='helloworld')
    # # result=request.COOKIES.get('is_login',0)
    # if result=='1':
    #     return render(request, 'app02/home.html')
    # else:
    #     return redirect('/login/')
    return render(request, 'app02/home.html')


@check_login
def index(request):
    # result = request.get_signed_cookie('is_login', 0, salt='helloworld')
    # # result=request.COOKIES.get('is_login',0)
    # if result == '1':
    #     return render(request, 'app02/index.html')
    # else:
    #     return redirect('/login/')
    return render(request, 'app02/index.html')


def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie('is_login')
    return rep
