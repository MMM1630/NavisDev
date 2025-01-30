from rest_framework import serializers
from .models import Consultation, Services, AboutUs, Tools, Projects, Reviews, Vacancy, JobApplication, Event, Gallery, \
    Category, Video


class ConsultationSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Consultation
        fields = ['phone_number', 'email', 'language']

class ServicesSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Services
        fields = ['image', 'sphere', 'title', 'industry','description', 'language']

class AboutsUsSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = AboutUs
        fields = ['title', 'image', 'description', 'language']

class ToolsSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Tools
        fields = ['name', 'image', 'language']

class ProjectsSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Projects
        fields = ['image', 'title', 'language']

class ReviewsSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Reviews
        fields = ['image', 'first_name', 'last_name', 'job_title', 'title','is_active' ,'language']

class VacancySerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        # fields = "__all__"
        # exclude = ['id']
        fields = ['id', 'level','job_title' ,'schedule','title_work' ,'title', 'language', 'content']



class JobApplicationSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = JobApplication
        fields = ['name', 'phone_number', 'email', 'urls']

class EventSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Event
        fields = ['image','topic' ,'title', 'date', 'time', 'location', 'description', 'date2' ,'time2', 'language']

class GallerySerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Gallery
        fields = ['language', 'img']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['project', 'vacancy', 'about_us', 'reviews', 'contacts']

class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['urls']