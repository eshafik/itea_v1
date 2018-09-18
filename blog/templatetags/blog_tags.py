from django import template
from django.db.models import Count
from blog.models import Post


register = template.Library()

#showing total blog post
@register.simple_tag
def total_posts():
    return Post.objects.published_posts().count()


#showing all latest post from render template
@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.published_posts().order_by('-publish')[:5]
    return {'latest_posts':latest_posts}

#showing latest post for members
@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts_for_member(count=5):
    latest_posts = Post.objects.filter(show_to='member' or 'public', status=True).order_by('-publish')[:5]
    return {'latest_posts':latest_posts}

#showing latest post for public
@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts_for_public(count=5):
    latest_posts = Post.objects.filter(show_to='public',status=True).order_by('-publish')[:5]
    return {'latest_posts':latest_posts}


#showing most commented posts
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.published_posts().annotate(total_comments=Count('comments')).order_by('-total_comments')[:5]