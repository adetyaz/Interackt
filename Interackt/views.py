from django.views.generic import TemplateView
from django.shortcuts import redirect


# Create your views here.
class TestPage(TemplateView):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        return redirect('posts:all')


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = 'index.html'
