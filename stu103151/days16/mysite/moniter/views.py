from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('This is moniter index')
def home(request):
    # return "asdf"
    user_info = [
        {'username':'alex1','name':'AlexLi1'},
        {'username':'alex2','name':'AlexLi2'},
        {'username':'alex3','name':'AlexLi3'},
        {'username':'alex4','name':'AlexLi4'},
    ]
    return render(request, 'moniter/t1.html', {'users': user_info})
def page1(request):
    return render(request,'moniter/t2.html',)
def page2(request):
    return render(request,'moniter/t3.html',)

def pay(request,user):
    print(user)
    return HttpResponse('paypal,%s' %user)

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