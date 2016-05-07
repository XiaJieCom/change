from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
# Create your views here.
from IDC import models
def login(request):
    user_list_obj = models.UserInfo.objects.all()
    return render(request, 'login.html', {'li': user_list_obj})
def check(request):
    i_username = request.POST.get('username')
    i_passwd = request.POST.get('password')
    # print(i_username,i_passwd)
    #查询用户名和密码,然后对比
    user_list_obj = models.UserInfo.objects.filter(username=i_username)
    for line in user_list_obj:
        # print(line.username,line.password)
        if line.password == i_passwd:
            ecs_list_obj = models.ECSInfo.objects.all()
            return render(request, 'ecs.html', {'li':ecs_list_obj})


        else:
            print('wrong!')
            return render(request, 'login.html', {'li': user_list_obj})

    # return HttpResponse('ok')



def db_handle(request):

    # 增加
    #1 直接指定对应的表,列和对应的数据
    #models.UserInfo.objects.create(username='alex', password='123', age=73)
    #2 定义一个字典,然后create
    # dic = {"username": 'eric', "password": '123', "age": 73}
    # models.UserInfo.objects.create(**dic)

    # 删除
    #删除指定条件的数据
    #models.UserInfo.objects.filter(username='alex').delete()

    # 修改
    #models.UserInfo.objects.all().update(age=18)

    # 查找
    #首先限定条件,确定要查找哪些信息;
    #循环打印
    #查找全部
    #models.UserInfo.objects.all()
    #根据具体条件查找
    #user_list_obj = models.UserInfo.objects.filter(username='eric')
    #查找第一条
    # user_list_obj = models.UserInfo.objects.filter(age=18).first()
    # print(type(user_list_obj))
    # print(user_list_obj)
    #输出
    # for line in user_list_obj:
    #     print(line.username,line.age)

    #
    # if request.method == "POST":
    #     models.ECSInfo.objects.create(host=request.POST['host'],
    #                                   ip=request.POST['ip'],
    #                                   port=request.POST['port'],)
    if request.method == "POST":
        if len(request.POST['host']) == 0 :
            print('no')
        else:
            print(request.POST['host'])
            print('no')
            models.ECSInfo.objects.create(host=request.POST['host'],
                                       ip=request.POST['ip'],
                                       port=request.POST['port'],
                                      status=request.POST['status'])

    ecs_list_obj = models.ECSInfo.objects.all()
    # for line in ecs_list_obj:
    #     print(line.host,line.ip)
    return render(request, 'ecs.html', {'li':ecs_list_obj})
    # return HttpResponse('ok')

def db_del(request):
    if request.method == "POST":
        print(request.POST['host'])
        models.ECSInfo.objects.filter(host=request.POST['host']).delete()

    ecs_list_obj = models.ECSInfo.objects.all()
    # for line in ecs_list_obj:
    #     print(line.host,line.ip)
    return render(request, 'ecs.html', {'li':ecs_list_obj})
    # return HttpResponse('ok')
