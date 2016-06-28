from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from  bbs import models
import json
from bbs import comment_hander
from bbs.forms import ArticleForm,handle_uploaded_file

# Create your views here.
def acc_login(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            #pass authentication
            login(request,user)
            return HttpResponseRedirect(request.GET.get('next') or '/bbs')
        else:
            login_err = "Wrong username or password!"
            return render(request,'login.html',{'login_err':login_err})
    return render(request,'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/bbs')

category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')
def index(request):
    category_obj = models.Category.objects.get(position_index=1)
    article_list = models.Article.objects.filter(status='published')
    return render(request,'bbs/index.html',{'category_list':category_list,
                                            'article_list':article_list,
                                            'category_obj':category_obj,
                                            })


def category(request,id):
    # print(request.POST)
    category_obj = models.Category.objects.get(id=id)
    if category_obj.position_index == 1:#首页
        article_list = models.Article.objects.filter(status='published')
    else:
        article_list = models.Article.objects.filter(category_id = category_obj.id,status='published')
    return render(request,'bbs/index.html',{'category_list':category_list,
                                            'category_obj':category_obj,
                                            'article_list':article_list
                                            })

def article_detail(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    comment_tree = comment_hander.build_tree(article_obj.comment_set.select_related())
    return render(request,'bbs/article_detail.html',{'article_obj':article_obj,
                                                     'category_list':category_list,})
def new_article(request):
    if request.method == 'POST':
        print(request.POST)
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            print('--form data',form.cleaned_data)
            form_data = form.cleaned_data
            form_data['author_id'] = request.user.userprofile.id
            new_img_path = handle_uploaded_file(request,request.FILES['head_img'])
            form_data['head_img'] = new_img_path
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return render(request,'bbs/new_article.html',{'new_article_obj':new_article_obj})
        else:
            print('err!!!',form.errors)
    category_list = models.Category.objects.all()
    return  render(request,'bbs/new_article.html',{'category_list':category_list
                                                   })

def comment(request):
    print(request.POST)
    if request.method == 'POST':
        new_comment_obj = models.Comment(
                article_id = request.POST.get('article_id'),
                parent_comment_id = request.POST.get('parent_comment_id') or None,
                comment_type = request.POST.get("comment_type"),
                user_id = request.user.userprofile.id,
                comment = request.POST.get('comment')
        )
        new_comment_obj.save()

        return HttpResponse('post-comment-success')
def get_comments(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    comment_tree = comment_hander.build_tree(article_obj.comment_set.select_related())
    tree_html = comment_hander.render_comment_tree(comment_tree)
    return HttpResponse(tree_html)







