from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
# Create your views here.
from app01 import models
def db_handle(request):
    return redirect('/app02/home/')
    # request 用户请求的所有内容
    # request.POST  用户以POST提交
    # request.GET  用户以POST提交
    # 增加
    # models.UserInfo.objects.create(username='alex', password='123', age=73)
    # dic = {"username": 'eric', "password": '123', "age": 73}
    # models.UserInfo.objects.create(**dic)
    # 删除
    # models.UserInfo.objects.filter(username='alex').delete()
    # 修改
    # models.UserInfo.objects.all().update(age=18)
    # 查找
    # models.UserInfo.objects.all()
    # models.UserInfo.objects.filter(age=18)
    # models.UserInfo.objects.filter(age=18).first()
    # user_list_obj = models.UserInfo.objects.all()
    # queryset,list
    # for line in user_list_obj:
    #     print(line.username,line.age)

    # return HttpResponse('ok')
    if request.method == "POST":
        print(request.POST)
        # request.POST['uername']
        # request.POST['uername']
        # request.POST['uername']
        # request.POST['age'] = int(request.POST['age'])
        # d = dict(request.POST)
        # models.UserInfo.objects.create(**d)
        models.UserInfo.objects.create(username=request.POST['username'],
                                       password=request.POST['password'],
                                       age=request.POST['age'])
    user_list_obj = models.UserInfo.objects.all()
    return render(request, 't1.html', {'li': user_list_obj})

def home(request):
    # return "asdf"
    return HttpResponse('App01.home')

def ajax_req(request):
    # return "asdf"
    # request.POST
    return HttpResponse('OK')

def news(request,nid2, nid1):
    # return "asdf"
    nid = nid1 + nid2
    return HttpResponse(nid)

def page(request,n2, n1):
    # return "asdf"
    nid = n1 + n2
    return HttpResponse(nid)