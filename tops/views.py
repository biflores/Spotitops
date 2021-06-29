# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


# if you set the template_name attribute, a GET request to that view will
# automatically use the defined template
class AboutPageView(TemplateView):
    template_name = "about.html"
