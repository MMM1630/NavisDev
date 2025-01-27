from rest_framework import serializers
from .models import Consultation, Services, AboutUs, Tools, Projects, Reviews, Vacancy, JobApplication, Event, Gallery


class ConsultationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['phone_number', 'email', 'language']

class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['image', 'sphere', 'title', 'industry', 'design', 'analysis', 'framework', 'img_framework','additionUI', 'img_additionUI', 'language']

class AboutsUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['title', 'image', 'description', 'language']

class ToolsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = ['name', 'image', 'language']

class ProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['image', 'title', 'language']

class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['image', 'first_name', 'last_name', 'job_title', 'title', 'language']

class VacancySerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['level','job_title' ,'schedule', 'title', 'title_work','description', 'responsibilities', 'requirements', 'working_conditions', 'language']

class JobApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['name', 'phone_number', 'email', 'urls']

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['image','topic' ,'title', 'date', 'time', 'location', 'description', 'requirements', 'date2' ,'time2', 'language']

class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['language', 'img']

