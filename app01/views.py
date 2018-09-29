from django.shortcuts import render,redirect,HttpResponse
from django.http import  JsonResponse
from app01 import models


# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        if username=='zhangsan' and password=='123456':
            return render(request,'transfer.html')

    return render(request,'login.html')

def transfer(request):
    if request.method=='POST':
        from_=request.POST.get("from")
        to_ = request.POST.get("to")
        money=request.POST.get("money")

        print("{}给{}转账{}".format(from_,to_,money))
        return HttpResponse("successfully")
    return render(request,'transfer.html')


def books(request):
    # #丛url中获取page_num
    # #三要素  总条数  显示的数  当前页
    page_num=request.GET.get("pn")
    # #总数量
    total_count=models.Book.objects.all().count()
    # #每页显示的数量
    per_page=10
    #
    # #总页数
    #
    # total_page,m=divmod(total_count,per_page)
    # if m:
    #     total_page+=1
    # #如果输入的页码数超过了最大的页码数，默认返回最后一页
    # try:
    #     page_num = int(page_num)
    #     if page_num>total_page:
    #         page_num=total_page
    # except Exception as e:
    #     #当输入的页码不是数字的时候，默认返回第一页
    #     page_num=1
    #
    # #数据是根据当前页查找数据的起点和重点
    # data_start=(page_num-1)*10
    # data_end=(page_num)*10
    #
    # #定义页面上的页码 11 个页码
    # max_page=11
    # #当我的最大页数小于页面中页码的个数的时候  当前最大的页数赋值给页码
    # if total_page<max_page:
    #     max_page=total_page
    #
    # half_max_page=max_page//2
    #
    # #页码上的页码开始的索引=
    # page_start=page_num-half_max_page
    #
    # page_end=page_num+half_max_page
    #
    # #判断
    # if page_start<=1:
    #     page_start=1
    #     page_end=max_page
    #
    # if page_end>total_page:
    #     page_end=total_page
    #     page_start=total_page-max_page+1
    #
    #
    # result=models.Book.objects.all()[data_start:data_end] #django分页就是切面
    #
    # #自己拼接分页的HTML
    # html_str_list=[]
    #
    # html_str_list.append('<li><a href="/books/?pn=1" >首页</a></li>')
    #
    # if page_num<=1:
    #     html_str_list.append('<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
    # else:
    #     html_str_list.append('<li><a href="/books/?pn={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num-1))
    #
    #
    # for i in range(page_start,page_end+1):
    #     if i==page_num:
    #         html_str_list.append('<li class="active"><a href="/books/?pn={0}">{0}</a></li>'.format(i))
    #     else:
    #         html_str_list.append('<li><a href="/books/?pn={0}">{0}</a></li>'.format(i))
    #
    # if page_num>=total_page:
    #     html_str_list.append('<li style="display:none"><a href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>')
    # else:
    #     html_str_list.append( '<li><a href="/books/?pn={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(page_num+1))
    #
    # html_str_list.append('<li><a href="/books/?pn={}" >尾页</a></li>'.format(total_page))
    #
    #
    #
    #
    # page_html="".join(html_str_list)

    #调用通用的模块 page_num,total_count,url_prefix,per_page=10,max_page=11
    from util.PageUtil import Page

    page_obj=Page(page_num,total_count,'books',per_page=10,max_page=11)

    result=models.Book.objects.all()[page_obj.data_start:page_obj.data_end]

    page_html=page_obj.page_html()


    return render(request,'books.html',{'books':result,'page_html':page_html})

