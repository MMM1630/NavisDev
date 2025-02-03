from rest_framework import serializers
from .models import Consultation, Services, AboutUs, Tools, Projects, Reviews, Vacancy, JobApplication, Event, Gallery, \
 Video

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = "__all__"


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"

class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"

class ToolsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = "__all__"

class ProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"

class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"

class VacancySerializers(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = "__all__"



class JobApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"