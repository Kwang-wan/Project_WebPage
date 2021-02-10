from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import render

from page.models import Member, Post, Photo, Tag, Category

from django.conf import settings

from page.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

class PageMemberDV(DetailView):
    template_name = 'page/member_detail.html'
    model = Member

class PageCategoryDV(DetailView):
    template_name = 'page/member_category_detail.html'
    model = Member

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoryname'] = self.kwargs['category_id']
        return context

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

#--- FormView
class SearchFormView(FormView): 
    form_class = PostSearchForm 
    template_name = 'page/post_search.html' 

    def form_valid(self, form): 
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {} 
        context['form'] = form 
        context['search_term'] = searchWord 
        context['object_list'] = post_list 

        return render(self.request, self.template_name, context)   # No Redirection