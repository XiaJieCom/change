from django.conf.urls import url,include
from django.contrib import admin
from webchat import views

urlpatterns = [
    url(r'^$', views.dashboard,name='chat_dashboard'),
    url(r'^msg_send/$', views.send_msg,name='send_msg'),
    url(r'^new_msgs/$', views.get_new_msgs,name='get_new_msgs'),
    url(r'^file_upload/$', views.file_upload,name='file_upload'),
    url(r'^file_upload_progress/$', views.get_file_upload_progress,name='file_upload_progress'),
    url(r'^delete_cache_key/$', views.delete_cache_key,name='delete_cache_key'),
]
