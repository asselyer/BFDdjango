from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import ListForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Comment.objects.all
            messages.success(request, ('Task Has Been Added'))
            return render(request, 'postlist.html', {'all_items': all_items})

    else:
        all_items = Comment.objects.all
        return render(request, 'postlist.html', {'all_items': all_items})


def postlist(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/postlist.html', {'posts': posts})