from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from collections import defaultdict
from navis.models import Video, Services, AboutUs, Tools, Projects, Reviews, Vacancy, Event, Gallery
from navis.serializers import ServicesSerializers, ToolsSerializers, ProjectsSerializers, ReviewsSerializers, VacancySerializers, JobApplicationSerializers, \
    EventSerializers, GallerySerializers,VideoSerializers, AboutUsSerializers, \
    ConsultationSerializer


class ConsultationView(generics.GenericAPIView):
    serializer_class = ConsultationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicesView(APIView):
    def get(self, request):
        services = Services.objects.all()
        serializer = ServicesSerializers(services, many=True)
        return Response(serializer.data)

class AboutUsView(APIView):
    def get(self, *args, **kwargs):
        queryset = AboutUs.objects.all()
        serializer = AboutUsSerializers(queryset, many=True)
        return Response(serializer.data)

class ToolsView(APIView):
    def get(self, request):
        tools = Tools.objects.all()
        serializer = ToolsSerializers(tools, many=True)
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

        grouped_data = defaultdict(list)
        for vacancy, data in zip(vacancies, serializer.data):
            grouped_data[vacancy.job_title].append(data)

        return Response(grouped_data)

class JobApplicationView(generics.GenericAPIView):
    serializer_class = JobApplicationSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Deserialize input data
        if serializer.is_valid():
            serializer.save()  # Save the new object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers

    # def get(self, request, *args, **kwargs):
    #     events = Event.objects.all()
    #     serializer = EventSerializers(events, many=True)
    #     return Response(serializer.data)

class GalleryView(APIView):
    def get(self, request, *args, **kwargs):
        gallery = Gallery.objects.all()
        serializer = GallerySerializers(gallery, many=True)
        return Response(serializer.data)

class VideoView(APIView):
    def get(self, request, *args, **kwargs):
        gallery = Video.objects.all()
        serializer = VideoSerializers(gallery, many=True)
        return Response(serializer.data)