from rest_framework import serializers
from .models import Consultation, Services, AboutUs, Tools, Projects, Reviews, Vacancy, JobApplication, Event, Gallery, \
 Video, Urls_to_social_network, UploadedFile
import os


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

    def validate_file(self, file):
        allowed_types = {'application/pdf', 'image/svg+xml', 'image/png'}
        allowed_extensions = {'pdf', 'svg', 'png'}

        if file:
            # Проверяем MIME-тип
            if file.content_type not in allowed_types:
                raise serializers.ValidationError(
                    f'Файл "{file.name}" имеет недопустимый формат! Разрешены только PDF, SVG, PNG.'
                )

            # Проверяем расширение файла
            ext = os.path.splitext(file.name)[1][1:].lower()
            if ext not in allowed_extensions:
                raise serializers.ValidationError(
                    f'Файл "{file.name}" имеет недопустимое расширение! Разрешены только .pdf, .svg, .png.'
                )  # ← Закрыл кавычки

        return file


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


class Urls_to_social_networkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Urls_to_social_network
        fields = "__all__"

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = "__all__"
