from django.views.generic import TemplateView, ListView
from page.models import Member

class HomeView(TemplateView):
    template_name = 'home.html'

class BaseLV(ListView):
    template_name = 'base.html'
    model = Member

    context_object_name = "members"