from django.views.generic import ListView, DetailView
from django.shortcuts import render

from page.models import Member, Post, Photo, Tag, Category

class PageLV(ListView):
    template_name = 'page/member_list.html'
    model = Member
    '''
    def get_queryset(self):
        return Member.objects.filter(name__name=self.kwargs.get('name'))
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_name'] = self.kwargs['name']
        return context

class PageCaLV(ListView):
    template_name = 'page/member_category_list.html'
    model = Post
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_name'] = self.kwargs['name']
        context['category_name'] = self.kwargs['category']
        return context   

class PageDV(DetailView):
    template_name = 'page/member_post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_name'] = self.kwargs['name']
        context['category_name'] = self.kwargs['category']
        context['post_name'] = self.kwargs['title']
        return context    

class PagePhotoDV(DetailView):
    template_name = 'page/member_photo_detail.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_name'] = self.kwargs['name']
        context['category_name'] = self.kwargs['category']
        context['post_name'] = self.kwargs['title']
        context['photo_name'] = self.kwargs['photo_title']
        return context    

class TagLV(ListView):
    template_name = 'tag/tag_list.html'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['tag']
        return context 

class CaLV(ListView):
    template_name = 'category/category_list.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.kwargs['category']
        return context 