from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static
from .sitemap import SitemapView
from django.conf import settings
from navis.views import ConsultationView, ServicesView, AboutUsView, ToolsView, ProjectsView, ReviewsView, \
    VacancyView, JobApplicationView, EventListView, GalleryView, VideoView, Urls_to_social_networkView, FileUploadView


schema_view = get_schema_view(
    openapi.Info(
        title="Navis Devs",
        default_version='v1',
        description="Документация Navis Devs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("consultation/", ConsultationView.as_view()),
    path('services', ServicesView.as_view()),
    path('aboutUsView/', AboutUsView.as_view()),
    path('tools/', ToolsView.as_view()),
    path('projects', ProjectsView.as_view()),
    path('reviews', ReviewsView.as_view()),
    path('vacancy', VacancyView.as_view()),
    path('jobApplication', JobApplicationView.as_view()),
    path('events', EventListView.as_view()),
    path('gallery', GalleryView.as_view()),
    path('youtube', VideoView.as_view()),
    path('Urls_to_social_network', Urls_to_social_networkView.as_view()),
    path('upload/', FileUploadView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path("sitemap.xml", SitemapView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    