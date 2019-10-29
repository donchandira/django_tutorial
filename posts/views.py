from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse('Hello from POSTS')
    return render(request, 'posts/index.html')
