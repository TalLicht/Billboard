from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('Billboard_site/index.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})