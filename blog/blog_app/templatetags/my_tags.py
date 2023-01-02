# isn't used. just as analog of using {% include %}  
from urllib import request
from django import template
from ..models import Category, Post, Tag, Comment
from ..forms import NewComment
from django.shortcuts import redirect
from django.core.paginator import Paginator

register = template.Library()

@register.simple_tag()
def show_categories():
    return Category.objects.all()

@register.inclusion_tag('blog_app/special_posts.html')
def special_posts(slic1=5, slic2=5):
    popular_posts = Post.objects.order_by('-views')[:slic1]
    recent_posts = Post.objects.order_by('-created_at')[:slic2]
    return {'popular_posts': popular_posts, 'recent_posts': recent_posts}

@register.inclusion_tag('blog_app/tags_cloud.html')
def tags():
    tags = Tag.objects.all()
    return {'tags': tags}

@register.inclusion_tag('blog_app/search.html')
def search_form():
    return

@register.inclusion_tag('blog_app/comments.html')
def show_comments(obj, page):
    # initial_data ={'post':obj}
    # paginator = Paginator(obj.comment_set.all(), 2)
    # page_obj = paginator.page(request.Get.get('page'))
    # return {'comments': obj.comment_set.all(), 'form': NewComment(initial_data), 'obj':obj, 'page_obj':page_obj}

    
    initial_data ={'post':obj}
    paginator = Paginator(obj.comment_set.all(), 2)
    comments = paginator.get_page(page)
    return {'comments': comments, 'form': NewComment(initial_data), 'obj':obj}
    
    # NewComment(initial_data) allows to create new form with placeholder