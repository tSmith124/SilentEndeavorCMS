from django.http import HttpResponse

def index(request):
    return HttpResponse("Home Page")

def posts(request):
    return HttpResponse("Posts")