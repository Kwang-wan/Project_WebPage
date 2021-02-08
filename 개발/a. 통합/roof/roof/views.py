from django.views.generic import TemplateView, ListView
from page.models import Member

class HomeView(TemplateView):
    template_name = 'home.html'

class BaseLV(ListView):
    template_name = 'base.html'
    model = Member

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_name'] = self.kwargs['name']
        return context