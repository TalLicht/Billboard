from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from datetime import datetime
from django.utils import timezone

def index(request):
    posts = Post.objects.all()
    return render(request,"Billboard_site/index.html",{'posts': posts})


def newpost(request):
    title = request.POST.get("title")
    text = request.POST.get("text")
    author = request.POST.get("author")
    pub_date = timezone.now()
    post = Post.objects.create(title=title, post_text=text, author=author, pub_date=pub_date)
    return render(request, "Billboard_site/index.html", {'post': post})