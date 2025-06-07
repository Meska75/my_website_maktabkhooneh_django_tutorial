from django import template
from blog.models import Post
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