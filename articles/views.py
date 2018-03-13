from django.shortcuts import render
from datetime import datetime
from .models import *
# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def add_post(request):
    info = " "
    if 'ok' in request.POST:
        try:
            title = request.POST['title']
            content = request.POST['content']
            Post.objects.create(title = title, content = content)
            info = " 新增成功"
        except:
            info = "新增失敗"

    return  render(request, 'add.html', {'info': info})
