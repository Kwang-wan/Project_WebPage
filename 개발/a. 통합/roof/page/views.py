from django.views.generic import ListView, DetailView
from django.shortcuts import render

class PageLV(ListView):
    pass
'''
    template_name = 'page/member_list.html'
    model = Category

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
'''
class PageCaLV(ListView):
    pass

class PageDV(DetailView):
    pass

class PagePhotoDV(DetailView):
    pass

class TagLV(ListView):
    pass

class CaLV(ListView):
    pass
