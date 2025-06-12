from django import template
from blog.models import Post
from django.utils import timezone


register = template.Library()

@register.inclusion_tag('website/web-recentposts.html')
def web_recent_posts():
    post = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-published_date')[:6]
    return {'recent_posts':post}