from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from navis.models import Consultation, Services, AboutUs, Tools, Projects, Reviews, Vacancy, Event, Gallery, Category
from navis.serializers import ConsultationSerializers, ServicesSerializers, AboutsUsSerializers, ToolsSerializers, \
    ProjectsSerializers, ReviewsSerializers, VacancySerializers, JobApplicationSerializers, \
    EventSerializers, GallerySerializers, CategorySerializers, VideoSerializers


class ConsultationView(APIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializers

    def post(self, request):
        serializer = ConsultationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServicesView(APIView):
    def get(self, request):
        services = Services.objects.all()
        serializer = ServicesSerializers(services, many=True)  # Сериализуем данные
        return Response(serializer.data)

class AboutUsView(APIView):
    def get(self, *args, **kwargs):
        queryset = AboutUs.objects.all()
        serializer = AboutsUsSerializers(queryset, many=True)
        return Response(serializer.data)

class ToolsView(APIView):
    def get(self, request):
        tools = Tools.objects.all()
        serializer = ToolsSerializers(tools, many=True)  # Сериализуем данные
        return Response(serializer.data)

class ProjectsView(APIView):
    def get(self, request):
        project = Projects.objects.get(id=1)
        serializer = ProjectsSerializers(project)
        return Response(serializer.data)

class ReviewsView(APIView):
    def get(self, request):
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializers(reviews, many=True)
        return Response(serializer.data)

class VacancyView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializers(vacancies, many=True)
        return Response(serializer.data)

class JobApplicationView(APIView):
    def post(self, request):
        serializer = JobApplicationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventListView(APIView):
    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializer = EventSerializers(events, many=True)
        return Response(serializer.data)

class GalleryView(APIView):
    def get(self, request, *args, **kwargs):
        gallery = Gallery.objects.all()
        serializer = GallerySerializers(gallery, many=True)
        return Response(serializer.data)

class CategoryView(APIView):
    def get(self, request, *args, **kwargs):
        gallery = Category.objects.all()
        serializer = CategorySerializers(gallery, many=True)
        return Response(serializer.data)

class VideoView(APIView):
    def post(self, request):
        serializer = VideoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)