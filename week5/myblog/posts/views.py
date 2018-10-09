from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, Http404
from .models import Post
from .forms import PostForm, CommentForm
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    sel = '<b>%s</b>' %('Привет')
    return HttpResponse(sel)

def form_o(request):
    data = {'bo':'bds'}
    if request.method == 'POST':
        mes = request.POST.get('gmes')
        data={'mes': mes}
    print(data)
    return render(request, 'posts/form.html', data)


def post_create(request):
    post_form = PostForm()

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            created_post = post_form.save(commit=True)
            return HttpResponseRedirect(reverse('posts:post_det', kwargs={'pk':created_post.id}))
    return render(request, 'posts/post_create.html', context={'form':post_form})

def post_list(request):
    posts_list = Post.objects.all()
    return render(request, 'posts/post_list.html', {'post_list':posts_list})

def post_det(request, pk):
    post = Post.objects.get(pk=pk)
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()

    return render(request, 'posts/det.html', context={'post':post, 'form':comment_form})

def home(request):
    return render(request, 'base.html')