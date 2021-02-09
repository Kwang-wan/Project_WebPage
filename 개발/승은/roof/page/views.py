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

from django.views.generic import FormView
from django.db.models import Q
from django.conf import settings
from page.forms import PostSearchForm

class SearchFormView(FormView): 
    form_class = PostSearchForm 
    template_name = 'page/post_search.html' 

    def form_valid(self, form): 
        # 제출된 값은 POST로 전달됨
        
        searchWord = form.cleaned_data['search_word']
        # cleaned_data = 검증에 통과한 값을 사전타입으로 제공 # 사용자가 입력한 검색 단어를 변수에 저장 

        post_list = Post.objects.filter(Q(title__icontains=searchWord) |  Q(title__icontains=searchWord) | Q(category_id__icontains=searchWord)).distinct()
        # Post의 객체중 제목이나 설명이나 내용에 해당 단어가 대소문자관계없이(icontains) 속해있는 객체를 필터링
        # distinct() = 중복 제외 # Q객체는 |(or)과 &(and) 두개의 operator와 사용가능
        context = {} 
        # context에 form객체, 즉 PostSearchForm객체 저장
        context['form'] = form 
        context['search_term'] = searchWord 
        context['object_list'] = post_list 

        return render(self.request, self.template_name, context) 