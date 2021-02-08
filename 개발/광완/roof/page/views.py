from django.views.generic import ListView, DetailView
from django.shortcuts import render

from page.models import Member, Post, Photo, Tag, Category

class PageLV(ListView):
    template_name = 'page/member_list.html'
    model = Member

class PageCaLV(ListView):
    template_name = 'page/member_category_list.html'
    model = Post 

class PageDV(DetailView):
    template_name = 'page/member_post_detail.html'
    model = Post

class PagePhotoDV(DetailView):
    template_name = 'page/member_photo_detail.html'
    model = Photo  

class TagLV(ListView):
    template_name = 'tag/tag_list.html'
    model = Tag

class CaLV(ListView):
    template_name = 'category/category_list.html'
    model = Category
