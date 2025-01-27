from django.views.generic import TemplateView
from .models import Services
from django.http import HttpResponse
from django.template.loader import render_to_string

class SitemapView(TemplateView):
    template_name = 'sitemapxml.html'
    content_type = "application/xml"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Services.objects.all().order_by('updated_at')
        return context

    def render_to_response(self, context, **kwargs):
        xml_content = render_to_string(self.template_name, context)
        return HttpResponse(xml_content, content_type=self.content_type)

