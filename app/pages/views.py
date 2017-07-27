# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from django.http import Http404, HttpResponsePermanentRedirect

from app.pages.models import Page


class PageDetailView(DetailView):
    context_object_name = 'page'
    queryset = Page.get_published.all()

    def get(self, request, *args, **kwargs):
        if not request.path.endswith('/'):
            return HttpResponsePermanentRedirect('%s/' % request.path)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        # context['meta'] = self.object.as_meta(self.request)
        return self.render_to_response(context)

    def get_template_names(self):
        template_name = 'pages/page.html'
        return template_name
