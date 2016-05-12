from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
# Create your views here.
def year(request):
    return HttpResponse('2003 year')
def years(request,year):
    return HttpResponse(' -> %s' %year)
def months(request,year,month):
    return HttpResponse(' -> %s.%s' %(year,month))
def id(request,year,month,id):
    return HttpResponse(' -> %s.%s_%s' %(year,month,id))
def type(request,year,month,id,type):
    return HttpResponse(' -> %s.%s_%s.%s' %(year,month,id,type))