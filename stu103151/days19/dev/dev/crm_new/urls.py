
from django.conf.urls import url,include
from crm_new import views

urlpatterns = [
      url(r'^$', views.index),
      url(r'^index/$', views.index),
      url(r'^accounts/login/$', views.acc_login),
      url(r'^accounts/logout/$', views.acc_logout),
      url(r'^customer_del/$',views.customer_del),
      url(r'^customer/$',views.customer,name="customer_list"),
      url(r'^customer/(\d+)/$',views.customer_detail,name="customer_detail" ),
      url(r'^school_del/$',views.school_del),
      url(r'^school/$',views.school,name="school_list"),
      url(r'^school/(\d+)/$',views.school_detail,name="school_detail" ),
      url(r'^course/$',views.course,name="course_list"),
      url(r'^course_del/$',views.course_del),
      url(r'^course/(\d+)/$',views.course_detail,name="course_detail" ),
      url(r'^class_list/$',views.class_list,name="class_list"),
      url(r'^classlist_del/$',views.class_del),
      url(r'^class_list/(\d+)/$',views.class_detail,name="class_detail" ),
      url(r'^user/$',views.user,name="user_list"),
      url(r'^user_del/$',views.user_del),
      url(r'^user/(\d+)/$',views.user_detail,name="user_detail" ),
      url(r'^studyrecord_del/$',views.studyrecord_del),
      url(r'^studyrecord/$',views.studyrecord,name="studyrecord_list"),
      url(r'^studyrecord/(\d+)/$',views.studyrecord_detail,name="studyrecord_detail" ),
]
