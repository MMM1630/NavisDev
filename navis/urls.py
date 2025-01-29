from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static
from .sitemap import SitemapView
from django.conf import settings
from navis.views import ConsultationView, ServicesView, AboutUsView, ToolsView, ProjectsView, ReviewsView, \
    VacancyView, JobApplicationView, EventListView, GalleryView, CategoryView, VideoView

schema_view = get_schema_view(
    openapi.Info(
        title="Navis Devs",
        default_version='v1',
        description="Documentation of your API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('Consultation/', ConsultationView.as_view(), name='Consultation'),
    path('Services', ServicesView.as_view(), name='Services'),
    path('AboutUsView/', AboutUsView.as_view(), name='AboutUs'),
    path('Tools/', ToolsView.as_view(), name='ToolsView'),
    path('Projects', ProjectsView.as_view(), name='Projects'),
    path('Reviews', ReviewsView.as_view(), name='Reviews'),
    path('Vacancy', VacancyView.as_view(), name='Vacancy'),
    path('JobApplication', JobApplicationView.as_view(), name='JobApplication'),
    path('Events', EventListView.as_view(), name='Vacancy'),
    path('Gallery', GalleryView.as_view(), name='Gallery'),
    path('Category', CategoryView.as_view(), name='Category'),
    path('Youtube', VideoView.as_view(), name='Youtube'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("api/sitemap.xml", SitemapView.as_view(), name="sitemap"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)