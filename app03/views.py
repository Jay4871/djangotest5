from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django import http
from django import views
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from app03 import models
import json


# Create your views here.

# 装饰器 CBV  FBV  python 方法和函数 python函数编程
def check_login(func):
    def inner(request, *args, **kwargs):
        result = request.session.get('is_login')
        if result == '1':
            return func(request, *args, **kwargs)
        else:
            next_url = request.path_info
            return redirect('/app03/login/?next={}'.format(next_url))

    return inner


@csrf_exempt
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
                rep = redirect('/app03/home/')
            request.session['is_login'] = '1'
            request.session.set_expiry(100)
            print(request.session.session_key)  # 64
            # rep.set_cookie("is_login",'1',max_age=10)
            # rep.set_signed_cookie('is_login','1',salt='helloworld')
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
    rep = redirect('/app03/login/')
    request.session.clear_expired()
    request.session.flush()
    return rep


@method_decorator(check_login, name='get')
class UserInfo(views.View):
    @method_decorator(check_login)
    def get(self, request):
        return render(request, 'app02/userinfo.html')


def ajax_html(request):
    return render(request, 'ajax-old.html')


def ajax_method(request):
    print(request.POST)
    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
    else:
        num1 = request.GET.get("num1")
        num2 = request.GET.get("num2")
    result = int(num1) + int(num2)
    return HttpResponse(result)


def test(request):
    import time
    time.sleep(5)
    # url='https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2382369768,106104803&fm=26&gp=0.jpg';
    # return HttpResponse(url)
    # return render(request,'login.html')
    return HttpResponse("https://ss1.bdstatic.com")


def testJson(request):
    result = models.Person.objects.all()
    # person_list=[]
    # for i in result:
    #     person_list.append({"name":i.name,'age':i.age})
    #
    # import  json
    # s=json.dumps(person_list)
    # from django.core import serializers
    # s=serializers.serialize('json',result)
    # return HttpResponse(s)
    return render(request, 'sweetalert.html', {'persons': result})


def delete(request):
    del_id = request.POST.get("id")
    models.Person.objects.filter(id=del_id).delete()
    return HttpResponse('delete success')


def testest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        listvalues = request.POST.getlist('listvalues')

        print(name, listvalues, type(listvalues))

    return HttpResponse('test')


def checkuser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        result = models.Person.objects.filter(name=name)
        if result:
            ret = {
                'staus': 0,
                'info': '此用户已被注册'
            }
        else:
            ret = {
                'staus': 1,
                'info': '此用户可用'
            }
        ret = json.dumps(ret)
        print(ret)
        return HttpResponse(ret)

    return render(request, 'reg.html')


def reguser(request):
    error = {"name": "", 'password': ''}
    password = request.POST.get('age')

    if len(password) < 6:
        error['password'] = '密码不能小于6位'

    return render(request, 'reg.html', {'error': error})


from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    name = forms.CharField(
        max_length=10,
        label='name',
        error_messages={
            "required": '改字段不能为空',
            'max_length': '长度不能大于10', },
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )

    age = forms.CharField(
        max_length=10, label='age',

    )

    # password=forms.CharField(
    #     label='password',
    #     min_length=6,
    #     max_length=10,
    #     widget=widgets.PasswordInput(attrs={'class': 'form-control'},render_value=True),
    #     error_messages={
    #         'min_length':'密码长度必须大于6'
    #     }
    # )
    # email=forms.EmailField(
    #     label='邮箱',
    #     # widget=widgets.EmailInput
    # )
    # mobile=forms.CharField(
    #     label='手机',
    #     validators=[
    #         RegexValidator(r'^[0-9]+$','提出提示'),
    #         RegexValidator(r'^[0-9]+$', '提出提示')
    #     ]
    # )
    #
    city = forms.ChoiceField(
        choices=models.City.objects.all().values_list('id', 'name'),
        label='city',
        initial=1,
        widget=forms.widgets.Select

    )
    # gender=forms.ChoiceField(
    #     choices=((1,'男'),(2,'女')),
    #     label='gender',
    #     initial=1,
    #     widget=forms.widgets.RadioSelect
    # )

    # hobby=forms.MultipleChoiceField(
    #     choices=((1,'篮球'),(2,'女'),(3,'跑步')),
    #     label='hobby',
    #     initial=[1,3],
    #     widget=forms.widgets.SelectMultiple
    # )

    # rember = forms.ChoiceField(
    #     choices=((1, '篮球'), (2, '女'), (3, '跑步')),
    #     label='记住我',
    #     initial='checked',
    #     widget=forms.widgets.CheckboxInput
    # )


def register(request):
    form_obj = RegisterForm()

    if request.method == 'POST':
        form_obj = RegisterForm(request.POST)
        print('helloworld')
        # 数据交给form它会给我们进行后端的校验
        if form_obj.is_valid():
            print(form_obj.cleaned_data)

        models.Person.objects.create(**form_obj.cleaned_data)
        return HttpResponse("注册成功")

    return render(request, 'register.html', {'form_obj': form_obj})
