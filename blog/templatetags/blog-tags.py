from django import template
from blog.models import Post , Category
from django.utils import timezone


register = template.Library()


@register.simple_tag(name='posts_counter')
def function():
    post = Post.objects.filter(published_date__lte=timezone.now(), status=1).count()
    return post

@register.simple_tag(name='post_view')
def function(postid):
    post = Post.objects.get(id=postid)
    return post.counted_view

@register.inclusion_tag('blog/blog-popularposts.html')
def popular_posts():
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-counted_view')[:3]
    return {'popularposts':posts}

@register.inclusion_tag('blog/blog-lastposts.html')
def last_posts():
    last_posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-published_date')[:3]
    return {'last_posts':last_posts}

@register.inclusion_tag('blog/blog-categories.html')
def post_categories():
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-published_date')
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()       
    sorted_cat = sorted(cat_dict.items(), key=lambda item: item[1], reverse=True)
    return {'categories':dict(sorted_cat)}