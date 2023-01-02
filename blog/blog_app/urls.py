from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', separate_category, name='category'),
    path('post/<str:slugi>/', ThePost.as_view(), name='post'),
    path('tags/<str:slug>/', ThePostsByTag.as_view(), name='tag'),
    path('search/', SearchedPosts.as_view(), name='search'),
    path('form/', add_comment, name='add_com'),
]