from rest_framework import status, generics
from rest_framework.response import Response
from itertools import groupby
from navis.models import Video, Services, AboutUs, Tools, Projects, Reviews, Vacancy, Event, Gallery, Consultation
from navis.serializers import ServicesSerializers, ToolsSerializers, ProjectsSerializers, ReviewsSerializers, VacancySerializers, JobApplicationSerializers, \
    EventSerializers, GallerySerializers,VideoSerializers, AboutUsSerializers,ConsultationSerializer


class ConsultationView(generics.ListAPIView):
    serializer_class = ConsultationSerializer
    queryset = Consultation.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicesView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializers_class = ServicesSerializers

class AboutUsView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializers

class ToolsView(generics.ListAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializers

class ProjectsView(generics.ListAPIView):
    queryset =  Projects.objects.all()
    serializer_class = ProjectsSerializers

class ReviewsView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers


class VacancyView(generics.ListAPIView):
    serializer_class = VacancySerializers


    def list(self, request, *args, **kwargs):
        queryset = Vacancy.objects.all()
        sorted_vacancies = sorted(queryset, key=lambda x: x.job_title)
        grouped_vacancies = groupby(sorted_vacancies, key=lambda x: x.job_title)

        data = {}
        for key, group in grouped_vacancies:
            serialized_group = VacancySerializers(group, many=True).data
            data[key] = serialized_group

        return Response(data)


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

class GalleryView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers

class VideoView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers