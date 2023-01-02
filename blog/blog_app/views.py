
from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView
from  django.core.paginator import Paginator
from django.db.models import F
from .forms import NewComment
from django.shortcuts import redirect
from django.http import Http404, HttpRequest, HttpResponseNotFound
from django.views.generic.list import MultipleObjectMixin


# def index(request):
#     categories = Category.objects.all()
#     posts = Post.objects.all()
#     return render(request, 'blog_app/index.html',{'categories': categories, 'posts': posts})
# 
# or/using simple_tag 
def index(request):
    posts = Post.objects.order_by('-created_at')
    paginator = Paginator(posts, 6)
    page_obj = paginator.page(request.GET.get('page', 1))
    # page_n = request.Get.get('page', 1)
    # page_obj = paginator.get_page(page_n)
    
    return render(request, 'blog_app/index.html',{'page_obj': page_obj})

    # paginator = Paginator(news, 4)
    # page_number = request.GET.get('page', 1)# equals page to 1, if there is no page value
    # page_obj = paginator.get_page(page_number)
    
def separate_category(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category__title = category.title).order_by('-created_at')
    paginator = Paginator(posts, 4)
    page_obj = paginator.page(request.GET.get('page', 1))

    return render(request, 'blog_app/index.html',{'category': category, 'page_obj': page_obj})

class ThePost(DetailView):
    model = Post
    # slug_field = 'slug'
    slug_url_kwarg = 'slugi'

    
    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     # Post.objects.filter(pk= self.object.pk).update(views = F('views') + 1)
    #     context['posts'] = Post.objects.order_by('-views')[:5]
    #     self.object.views =F('views') + 1 
    #     self.object.save()
    #     self.object.refresh_from_db()
    #     context['form1'] = NewComment()
    #     object_list = Comment.objects.filter(post=self.get_object())
    #     context['object_list'] = object_list
    #     return context

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        # Post.objects.filter(pk= self.object.pk).update(views = F('views') + 1)
       
        self.object.views =F('views') + 1 
        self.object.save()
        self.object.refresh_from_db()
        page = self.request.GET.get('page', 1)
        context['page'] = page
        return context


class ThePostsByTag(ListView):
    template_name ='blog_app/index.html'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

class SearchedPosts(ListView):
    template_name = 'blog_app/index.html'
    paginate_by = 2
    model = Post

    def get_queryset(self):
        return Post.objects.filter(title__icontains= self.request.GET.get('looking_for'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['looking_for'] = f"looking_for={self.request.GET.get('looking_for')}&"
        return context

def add_comment(request):
    if request.method == 'POST':
        form = NewComment(request.POST)
        if form.is_valid():
            form.save()
    else:
        return HttpResponseNotFound("Page not found")
    return redirect(request.META.get('HTTP_REFERER'))
