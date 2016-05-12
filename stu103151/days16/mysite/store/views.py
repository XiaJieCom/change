from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from store import  models
# Create your views here.
def reg(request):
    if request.method == "POST":
        i_username = request.POST.get('username')
        i_passwd = request.POST.get('passwd')
        tmp_dic = models.UserInfo.objects.filter(username=i_username)
        if tmp_dic == 0:
            models.UserInfo.objects.create(username=i_username,
                                            password=i_passwd)
            ecs_list_obj = models.UserInfo.objects.all()
            return render(request, 'store/book_info.html', {'li':ecs_list_obj})
        else:
            print('用户名已存在')
            return HttpResponse('用户名已存在')
    else:
        return render(request, 'store/registry.html')
def login(request):
    user_list_obj = models.UserInfo.objects.all()
    return render(request, 'store/login.html', {'li': user_list_obj})
def check(request):
    i_username = request.POST.get('username')
    i_passwd = request.POST.get('password')
    #查询用户名和密码,然后对比
    user_list_obj = models.UserInfo.objects.filter(username=i_username)
    # print(user_list_obj)
    # return HttpResponse(user_list_obj)
    for line in user_list_obj:
        # print(line.username,line.password)
        if line.password == i_passwd:
            # ecs_list_obj = models.UserInfo.objects.all()
            # return render(request, 'store/book_info.html', {'li':ecs_list_obj})
            return HttpResponseRedirect('/store/home/')
        else:
            print('wrong!')
            return render(request, 'store/login.html', {'li': user_list_obj})

def home(request):
    # return HttpResponse('this is index')
    if request.method == 'POST':
        print(request.POST)
    else:
        return render(request,'store/start.html')
def books(request):
    books = models.Book.objects.all()
    author_list = models.Author.objects.all()
    print(books)
    print(author_list)
    # return render(request,'store/book_list.html',{'books':books})
    return render(request,'store/book_list.html',{'li':books})
def authors(request):
    author_list = models.Author.objects.all()
    return render(request,'store/author_list.html',{'li':author_list})
def publishers(request):
    publisher_list = models.Publisher.objects.all()
    return render(request,'store/publisher_list.html',{'li':publisher_list})

def author_edit(request):
    if request.method == 'POST':
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        models.Author.objects.create(first_name = first,
                                     last_name = last)
        author_list = models.Author.objects.all()
        return render(request,'store/author_list.html',{'li':author_list})


# def book(request):
#  if request.method == 'POST':
#         print(request.POST)
#         book_name = request.POST.get('name')
#         publisher_id = request.POST.get('publisher_id')
#         print('==>',request.POST.get('author_ids'))
#         author_ids = request.POST.getlist('author_ids')
#         #print(dir( request.POST))
#         print(book_name,publisher_id,author_ids)
#
#         new_book = models.Book(
#             name=book_name,
#             publisher_id = publisher_id,
#             publish_date = '2016-05-22'
#         )
#         new_book.save()
#         new_book.authors.add(*author_ids)
#         #new_book.authors.add(1,2,3,4)
#
#     books = models.Book.objects.all()
#     publisher_list = models.Publisher.objects.all()
#     author_list = models.Author.objects.all()
#
#
#     return render(request,'app01/book.html',{'books':books,
#                                                   'publishers':publisher_list,
#                                                  'authors':author_list
#                                                   })