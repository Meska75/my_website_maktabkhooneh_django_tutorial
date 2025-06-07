from django.utils import timezone
from django.shortcuts import render , get_object_or_404
from blog.models import Post

# Create your views here.

def blog_view(request, cat_name=None, author_username= None):
    if cat_name:
        post = Post.objects.filter(published_date__lte=timezone.now(), status=1,category__name=cat_name)
    elif author_username:
        post = Post.objects.filter(published_date__lte=timezone.now(), status=1,author__username=author_username)
    else:
        post = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    context = {'posts':post}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    post = get_object_or_404(Post,id=pid)
    all_posts = list(Post.objects.filter(published_date__lte=timezone.now(), status=1))
    try:
        index = next(i for i, p in enumerate(all_posts) if p.pk == post.pk)
    except StopIteration:
        index = None
    previous_post = None
    next_post = None
    if index is not None:
        if index > 0:
            next_post = all_posts[index - 1]
        if index < len(all_posts) - 1:
            previous_post = all_posts[index + 1]
    context = {'posts':post, 'prev_post': previous_post, 'next_post':next_post}
    post.counted_view += 1
    post.save()
    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    post = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if request.method == 'GET':
        post = post.filter(content__contains=request.GET.get('s'))


    context = {'posts':post}
    return render(request, 'blog/blog-home.html',context)
