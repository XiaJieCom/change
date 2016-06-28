from django.shortcuts import HttpResponse,HttpResponseRedirect,render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from crm_new import  models,forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from crm_new.permissions import check_permission
# Create your views here.
@login_required
def index(request):
    return render(request,'crm/lunch.html')
def acc_login(request):
    if request.method == 'POST':
        # print(request.POST)
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            #pass authentication
            login(request,user)
            return HttpResponseRedirect('/crm/index/')
        else:
            login_err = "Wrong username or password!"
            return render(request,'crm/login.html',{'login_err':login_err})
    return render(request,'crm/login.html')
def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/crm/index/')
@check_permission
def user(request):
    if request.method == 'POST':
        form = forms.UserProfileModelForm(request.POST)
        if form.is_valid():
            form.save()
    user_list = models.UserProfile.objects.all()
    pageinator = Paginator(user_list,3)
    page = request.GET.get('page')
    try:
        objs = pageinator.page(page)
    except PageNotAnInteger:
        objs = pageinator.page(1)
    except EmptyPage:
        objs = pageinator.page(pageinator.num_pages)
    form = forms.UserProfileModelForm()
    return render(request,'crm/user.html',{'user_list':objs,
                                           'model_form':form,
                                           })
@check_permission
def user_del(request):
    if request.method == 'POST':
        ids = request.POST.getlist('choice')
        for i in ids:
            models.UserProfile.objects.filter(id = i).delete()
        return HttpResponseRedirect('/crm/user/')
@check_permission
def user_detail(request,userprofile_id):
    base_url = "/".join(request.path.split("/")[:-2])
    user_obj = models.UserProfile.objects.get(id=userprofile_id)
    if request.method == "POST":
        form = forms.UserProfileModelForm(request.POST,instance=user_obj)
        #print(request.POST)
        if form.is_valid():
            form.save()
            print( 'url:',request.path)
            base_url = "/".join(request.path.split("/")[:-2])
            print( 'url:',base_url)
            return redirect(base_url)
        #else:
    else:
        form = forms.UserProfileModelForm(instance=user_obj)
    return render(request,'crm/base_detail.html',{'model_form':form,
                                                  'base_url':base_url,})
@check_permission
def customer(request):
    if request.method == 'POST':
        form = forms.CustomerModelForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
    customer_list = models.Customer.objects.all()
    pageinator = Paginator(customer_list,3)
    page = request.GET.get('page')
    try:
        customer_objs = pageinator.page(page)
    except PageNotAnInteger:
        customer_objs = pageinator.page(1)
    except EmptyPage:
        customer_objs = pageinator.page(pageinator.num_pages)
    form = forms.CustomerModelForm()
    return render(request,'crm/customers.html',{'customer_list':customer_objs,
                                                'model_form':form,
                                                })
def customer_del(request):
    if request.method == 'POST':
        ids = request.POST.getlist('choice')
        for i in ids:
            models.Customer.objects.filter(id = i).delete()
        return HttpResponseRedirect('/crm/customer/')

@check_permission
def customer_detail(request,customer_id):
    base_url = "/".join(request.path.split("/")[:-2])
    customer_obj = models.Customer.objects.get(id=customer_id)
    if request.method == "POST":
        form = forms.CustomerModelForm(request.POST,instance=customer_obj)
        #print(request.POST)
        if form.is_valid():
            form.save()
            print( 'url:',request.path)
            base_url = "/".join(request.path.split("/")[:-2])
            print( 'url:',base_url)
            return redirect(base_url)
        #else:
    else:
        form = forms.CustomerModelForm(instance=customer_obj)
    return render(request,'crm/base_detail.html',{'model_form':form,
                                                  'base_url':base_url,})

@check_permission
def school(request):
    if request.method == 'POST':
        form = forms.SchoolModelForm(request.POST)
        if form.is_valid():
            form.save()
    shcool_list = models.School.objects.all()
    pageinator = Paginator(shcool_list,4)
    page = request.GET.get('page')
    try:
        objs = pageinator.page(page)
    except PageNotAnInteger:
        objs = pageinator.page(1)
    except EmptyPage:
        objs = pageinator.page(pageinator.num_pages)
    form = forms.SchoolModelForm()
    return render(request,'crm/school.html',{'shcool_list':objs,
                                             'model_form':form
                                             })
@check_permission
def school_del(request):
    if request.method == 'POST':
        ids = request.POST.getlist('choice')
        for i in ids:
            models.School.objects.filter(id = i).delete()
        return HttpResponseRedirect('/crm/school/')
@check_permission
def school_detail(request,school_id):
    base_url = "/".join(request.path.split("/")[:-2])
    school_obj = models.School.objects.get(id=school_id)
    if request.method == "POST":
        form = forms.SchoolModelForm(request.POST,instance=school_obj)
        #print(request.POST)
        if form.is_valid():
            form.save()
            print( 'url:',request.path)
            base_url = "/".join(request.path.split("/")[:-2])
            print( 'url:',base_url)
            return redirect(base_url)
        #else:
    else:
        form = forms.SchoolModelForm(instance=school_obj)
    return render(request,'crm/base_detail.html',{'model_form':form,
                                                  'base_url':base_url,})

@check_permission
def course(request):
    if request.method == 'POST':
        print(request.POST)
        form = forms.CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('NO !!!')
    course_list = models.Course.objects.all()
    pageinator = Paginator(course_list,3)
    page = request.GET.get('page')
    try:
        course_objs = pageinator.page(page)
    except PageNotAnInteger:
        course_objs = pageinator.page(1)
    except EmptyPage:
        course_objs = pageinator.page(pageinator.num_pages)
    form = forms.CourseModelForm()
    return render(request,'crm/course.html',{'course_list':course_objs,
                                             'model_form':form
                                             })
@check_permission
def course_del(request):
    if request.method == 'POST':
        ids = request.POST.getlist('choice')
        for i in ids:
            models.Course.objects.filter(id = i).delete()
        return HttpResponseRedirect('/crm/course/')
@check_permission
def course_detail(request,course_id):
    base_url = "/".join(request.path.split("/")[:-2])
    course_obj = models.Course.objects.get(id=course_id)
    if request.method == "POST":
        form = forms.CourseModelForm(request.POST,instance=course_obj)
        #print(request.POST)
        if form.is_valid():
            form.save()
            print( 'url:',request.path)
            base_url = "/".join(request.path.split("/")[:-2])
            print( 'url:',base_url)
            return redirect(base_url)
        #else:
    else:
        form = forms.CourseModelForm(instance=course_obj)
    return render(request,'crm/base_detail.html',{'model_form':form,
                                                  'base_url':base_url,})
@check_permission
def class_list(request):
    if request.method == 'POST':
        print(request.POST)
        form = forms.ClassListModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('NO !!!')
    class_list = models.ClassList.objects.all()
    pageinator = Paginator(class_list,3)
    page = request.GET.get('page')
    try:
        objs = pageinator.page(page)
    except PageNotAnInteger:
        objs = pageinator.page(1)
    except EmptyPage:
        objs = pageinator.page(pageinator.num_pages)
    course_list = models.Course.objects.all()
    teachers_list = models.UserProfile.objects.all()
    form = forms.ClassListModelForm()
    return render(request,'crm/classlist.html',{'class_list':objs,
                                                'course_list':course_list,
                                                'teachers_list':teachers_list,
                                                'model_form':form
                                                })
@check_permission
def class_del(request):
    if request.method == 'POST':
        ids = request.POST.getlist('choice')
        for i in ids:
            models.ClassList.objects.filter(id = i).delete()
        return HttpResponseRedirect('/crm/classlist/')
@check_permission
def class_detail(request,classlist_id):
    base_url = "/".join(request.path.split("/")[:-2])
    classlist_obj = models.ClassList.objects.get(id=classlist_id)
    if request.method == "POST":
        form = forms.ClassListModelForm(request.POST,instance=classlist_obj)
        #print(request.POST)
        if form.is_valid():
            form.save()
            print( 'url:',request.path)
            base_url = "/".join(request.path.split("/")[:-2])
            print( 'url:',base_url)
            return redirect(base_url)
        #else:
    else:
        form = forms.ClassListModelForm(instance=classlist_obj)
    return render(request,'crm/base_detail.html',{'model_form':form,
                                                  'base_url':base_url,})
@check_permission
def studyrecord(request):
    studyrecord_list = models.StudyRecord.objects.all()
    pageinator = Paginator(studyrecord_list,3)
    page = request.GET.get('page')
    try:
        objs = pageinator.page(page)
    except PageNotAnInteger:
        objs = pageinator.page(1)
    except EmptyPage:
        objs = pageinator.page(pageinator.num_pages)
    return render(request,'crm/studyrecord.html',{'studyrecord_list':objs})
def studyrecord_del(request):
    if request.method == 'POST':
        ids = request.POST.getlist('choice')
        for i in ids:
            models.StudyRecord.objects.filter(id = i).delete()
        return HttpResponseRedirect('/crm/studyrecord/')

@check_permission
def studyrecord_detail(request,studyrecord_id):

    # print( 'url:',request.path)
    base_url = "/".join(request.path.split("/")[:-2])
    # print( 'url --->',base_url)
    studyrecord_obj = models.StudyRecord.objects.get(id=studyrecord_id)
    if request.method == "POST":
        form = forms.StudyRecordModelForm(request.POST,instance=studyrecord_obj)
        #print(request.POST)
        if form.is_valid():
            form.save()
            # print( 'url:',request.path)
            # base_url = "/".join(request.path.split("/")[:-2])
            # print( 'url:',base_url)
            return redirect(base_url)
        #else:
    else:
        form = forms.StudyRecordModelForm(instance=studyrecord_obj)
    return render(request,'crm/base_detail.html',{'model_form':form,
                                                  'base_url':base_url,
                                                  })