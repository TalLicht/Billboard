from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from datetime import datetime

def index(request):
    posts = Post.object.all()
    return render(request,"Billboard_site/index.html",posts)


def post(request):
    title = request.POST.get("title")
    text = request.POST.get("text")
    author = request.POST.get("author")
    pub_date = datetime.datetime.now()
    post = Post.objects.create(title=title, post_text=text, author=author, pub_date=pub_date)
    return render(request, "Billboard_site/index.html", {'post': post})