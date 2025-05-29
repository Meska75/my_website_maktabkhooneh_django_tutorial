from django.utils import timezone
from django.shortcuts import render , get_object_or_404
from blog.models import Post

# Create your views here.

def blog_view(request):
    post = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    context = {'posts':post}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    post = get_object_or_404(Post,id=pid)
    post.content_views += 1
    post.save()
    return render(request, 'blog/blog-single.html')

