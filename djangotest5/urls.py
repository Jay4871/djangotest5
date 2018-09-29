"""djangotest5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import  views as v1
from app02 import  views as v2
from app03 import  views as v3

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^transfer/$', v1.transfer),
    url(r'^books/$', v1.books),


    #cookie
    url(r'^login/$', v2.login),
    url(r'^home/$', v2.home),
    url(r'^index/$', v2.index),
    url(r'^logout/$', v2.logout),

    url(r'^app03/login/$', v3.login),
    url(r'^app03/home/$', v3.home),
    url(r'^app03/index/$', v3.index),
    url(r'^app03/logout/$', v3.logout),
    url(r'^app03/userinfo/$', v3.UserInfo.as_view()),

    url(r'^ajax_calc/$', v3.ajax_method),
    url(r'^ajax_html/$', v3.ajax_html),
    url(r'^test/$', v3.test),
    url(r'^testJson/$', v3.testJson),
    url(r'^delete/$', v3.delete),
    url(r'^testest/$', v3.testest),
    url(r'^reg/$', v3.checkuser),
    url(r'^reguser/$', v3.reguser),
    url(r'^register/$', v3.register),








]
