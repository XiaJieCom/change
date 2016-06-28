
from django.core.urlresolvers import resolve
from django.shortcuts import render,redirect

perm_dic = {
    'view_customer_list': ['customer_list','GET',[]],
    'view_customer_info': ['customer_detail','GET',[]],
    'edit_own_customer_info': ['customer_detail','POST',[]],
    'view_course_list': ['course_list','GET',[]],
    'view_course_info': ['course_detail','GET',[]],
    'edit_own_course_info': ['course_detail','POST',[]],
    'view_user_list': ['user_list','GET',[]],
    'view_user_info': ['user_detail','GET',[]],
    'edit_own_user_info': ['user_detail','POST',[]],
    'view_class_list': ['class_list','GET',[]],
    'view_class_info': ['class_detail','GET',[]],
    'edit_own_class_info': ['class_detail','POST',[]],
    'view_school_list': ['school_list','GET',[]],
    'view_school_info': ['school_detail','GET',[]],
    'edit_own_school_info': ['school_detail','POST',[]],
    'view_studyrecord_list': ['studyrecord_list','GET',[]],
    'view_studyrecord_info': ['studyrecord_detail','GET',[]],
    'edit_own_studyrecord_info': ['studyrecord_detail','POST',[]],
}

def perm_check(*args,**kwargs):
    request = args[0]
    url_resovle_obj = resolve(request.path_info)
    current_url_namespace = url_resovle_obj.url_name
    #app_name = url_resovle_obj.app_name #use this name later
    print("url namespace:",current_url_namespace)
    matched_flag = False # find matched perm item
    matched_perm_key = None
    if current_url_namespace is not None:#if didn't set the url namespace, permission doesn't work
        print("find perm...")
        for perm_key in perm_dic:
            perm_val = perm_dic[perm_key]
            if len(perm_val) == 3:#otherwise invalid perm data format
                url_namespace,request_method,request_args = perm_val
                print(url_namespace,current_url_namespace)
                if url_namespace == current_url_namespace: #matched the url
                    if request.method == request_method:#matched request method
                        if not request_args:#if empty , pass
                            matched_flag = True
                            matched_perm_key = perm_key
                            print('mtched...')
                            break #no need looking for  other perms
                        else:
                            for request_arg in request_args: #might has many args
                                request_method_func = getattr(request,request_method) #get or post mostly
                                #print("----->>>",request_method_func.get(request_arg))
                                if request_method_func.get(request_arg) is not None:
                                    matched_flag = True # the arg in set in perm item must be provided in request data
                                else:
                                    matched_flag = False
                                    print("request arg [%s] not matched" % request_arg)
                                    break #no need go further
                            if matched_flag == True: # means passed permission check ,no need check others
                                print("--passed permission check--")
                                matched_perm_key = perm_key
                                break

    else:#permission doesn't work
        return True

    if matched_flag == True:
        #pass permission check
        perm_str = "crm_new.%s" %(matched_perm_key)
        print(request.user)
        if request.user.has_perm(perm_str):
            print("\033[42;1m--------passed permission check----\033[0m")
            return True
        else:
            print("\033[41;1m ----- no permission ----\033[0m")
            print(request.user,perm_str)
            return False
    else:
        print("\033[41;1m ----- no matched permission  ----\033[0m")
def check_permission(func):

    def wrapper(*args,**kwargs):
        print("---start check perms",args[0])
        if not perm_check(*args,**kwargs):
            return render(args[0],'crm/403.html')
        else:
            print("---done check perms---")
            return func(*args,**kwargs)
    return wrapper

