from __future__ import absolute_import, division, print_function, unicode_literals

from mongoengine.queryset.visitor import Q

from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from rest_framework.filters import SearchFilter

from feed.serializer import FeedSerializer
from feed.models import News


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Contains scraped data from leading news portal.
    Q parameter is used to search for specific news information, will scan the mongodb 
    base on the parameter value stated on the url e.g. http://127.0.0.1/api/news/?q=Russia
    Lookup fields are headline, section, and news summary.
    '''
    lookup_field = 'id'
    serializer_class = FeedSerializer
    filter_backends = [SearchFilter]
    search_fields = ['headline', 'section', 'summary']

    def get_queryset(self):
        """
        Optionally restricts the returned list of scrapped news,
        filtering result against a `q`(search_keyword) query parameter in the URL.

        Improvement: use django-haystack and elasticsearch for optimum search functionality
        """
        queryset = News.objects.all()
        search_keyword = self.request.query_params.get('q', None)
        if search_keyword:
            queryset = queryset.filter(
                Q(headline__icontains=search_keyword) | 
                Q(section__icontains=search_keyword) | 
                Q(summary__icontains=search_keyword))

        return queryset

    def list(self, request, *args, **kwargs):
        search_page = self.get_queryset()
        serializer = self.get_serializer(search_page, many=True)
        return Response(serializer.data)
