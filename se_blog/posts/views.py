from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts


def allPosts(request):
    posts = Posts.objects.all().order_by("publish_date")
    return HttpResponse({'posts': posts})