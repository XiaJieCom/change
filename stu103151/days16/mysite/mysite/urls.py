"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin


#匹配原则,循环匹配,直到匹配的第一个

urlpatterns = [
    # url(r'^$', IDC.urls.index),
    url(r'^admin/', admin.site.urls),
    #url(r'^cmdb/', include("IDC.urls")),
    #全局给该url传参数
    url(r'^moniter/', include("moniter.urls")),
    url(r'^store/', include("store.urls")),




    #全局

    # url(r'^articles/2013/$', views.year),
    # #精确匹配
    # url(r'^articles/([0-9]{4})/$', views.years),
    # #模糊匹配年月
    # url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.months),
    # #模糊匹配文章id
    # url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.id),
    # #模糊匹配文件类型
    # url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+).(\w+)/$', views.type),

]