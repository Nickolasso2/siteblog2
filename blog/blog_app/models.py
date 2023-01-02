from ast import Delete
from pickle import TRUE
from tkinter import CASCADE
from turtle import mode
from django import views
from django.db import models
from django.urls import reverse
from  mptt.models import MPTTModel, TreeForeignKey

# class Category(MPTTModel)- клас, який буде створювати багаторівневе меню(БР)
class Category(MPTTModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)#

    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.title

    # def get_absolute_url(self):
    #     return reverse('tag', kwargs={'slug':self.slug})



class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photoes/%Y/%m/%d/')
    views = models.IntegerField(editable=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title

# class Comment(MPTTModel)- клас, який буде створювати багаторівневе меню(БР) коментів
class Comment(MPTTModel):
    author = models.CharField(max_length=50)
    commented_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')# поле вибору, батьківського елемента
    liked = models.IntegerField(default=0)
    reply_number = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)


   
    def __str__(self) -> str:
        return self.author