from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf import settings
from django.views.generic import TemplateView, ListView

from mongoengine.queryset.visitor import Q
from .models import News


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        news_listings = News.objects.all()
        context['news_listings'] = news_listings
        return context


class SearchNewsPage(ListView):
    template_name = "search.html"
    keyword = ''

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax() or request.GET.get('q'):
            self.keyword = request.GET.get('q')
        return super(SearchNewsPage, self).dispatch(request, *args, **kwargs)

    def get_template_names(self):
        return super(SearchNewsPage, self).get_template_names()

    def get_queryset(self):
        '''
        Improvement: use django-haystack and elasticsearch for optimum search functionality
        '''

        news = News.objects.all()
        if self.keyword:
            news = news.filter(
                Q(headline__icontains=self.keyword) | Q(
                    section__icontains=self.keyword) | Q(
                    summary__icontains=self.keyword))
        return news

    def get_context_data(self, **kwargs):
        context = super(SearchNewsPage, self).get_context_data(**kwargs)
        news_listings = self.get_queryset()
        context['search_result'] = news_listings
        context['keyword'] = self.keyword
        return context
