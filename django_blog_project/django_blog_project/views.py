from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

def index(request):
    #return HttpResponse('I am home page')
    return HttpResponseRedirect(reverse('app_blog:blog_list'))
