from django.conf.urls import url
from store import views
urlpatterns = [
    url(r'^$', views.login),
    # url(r'^db_handle/$',views.db_handle),
    url(r'^check/', views.check),
    url(r'^reg/', views.reg),
    url(r'^home/', views.home),
    url(r'^books/', views.books),
    url(r'^authors/', views.authors),
    url(r'^publishers/', views.publishers),
    url(r'^author_edit/', views.author_edit),


]
