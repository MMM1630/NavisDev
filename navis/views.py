from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
import requests
import os
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from itertools import groupby
from navis.models import Video, Services, AboutUs, Tools, Projects, Reviews, Vacancy, Event, Gallery, Consultation, JobApplication, Urls_to_social_network, UploadedFile
from navis.serializers import ServicesSerializers, ToolsSerializers, ProjectsSerializers, ReviewsSerializers, VacancySerializers, JobApplicationSerializers, \
    EventSerializers, GallerySerializers,VideoSerializers, AboutUsSerializers,ConsultationSerializer, Urls_to_social_networkSerializers, FileUploadSerializer


TELEGRAM_BOT_TOKEN = "7844581665:AAE7PiUMvblvxGDOggvNs-10cu1tK_a6Tl8"
TELEGRAM_CHAT_ID = "-4673876479"  

@method_decorator(csrf_exempt, name='dispatch')
class ConsultationView(generics.ListCreateAPIView):  
    serializer_class = ConsultationSerializer
    queryset = Consultation.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            consultation = serializer.save()

            try:
                message = (
                    f"💬 *Новая консультация!*\n\n"
                    f"👨‍💻/👩‍💻 *Имя* {consultation.name}\n"
                    f"📧 *Email* {consultation.email}\n"
                    f"📞 *Телефон* {consultation.phone_number}\n"
                    f"📝 *Сообщение* {consultation.message}"
                )

                url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": message,
                    "parse_mode": "Markdown"
                }

                response = requests.post(url, json=payload)

                if response.status_code == 200:
                    print("Message sent successfully!")
                else:
                    print(f"Failed to send message. Response: {response.text}")
            except Exception as e:
                print(f"Error sending message to Telegram: {e}")
                return Response({"error": "Failed to send message to Telegram"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicesView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers

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
    queryset = JobApplication.objects.all()
    parser_classes = (MultiPartParser, FormParser)  # Позволяет загружать файлы

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            jobApplication = serializer.save()
            
            message = (
                f"💬 *Заявление о приеме на работу!*\n\n"
                f"👨‍💻/👩‍💻 *Имя:* {jobApplication.name}\n"
                f"📞 *Телефон:* {jobApplication.phone_number}\n"
                f"📧 *Email:* {jobApplication.email}\n"
                f"🌐 *Ссылка на соц сеть:* {jobApplication.urls if jobApplication.urls else 'Нет'}\n"
                f"📁 *Прикрепленный файл:* {'Есть' if jobApplication.file else 'Нет прикрепленного файла'}\n"
            )

            text_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            text_payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "Markdown"
            }
            text_response = requests.post(text_url, json=text_payload)

            if text_response.status_code == 200:
                print("✅ Сообщение отправлено успешно!")
            else:
                print(f"❌ Ошибка при отправке сообщения: {text_response.text}")

            if jobApplication.file:
                file_path = jobApplication.file.path  
                print(f"📂 Отправка файла: {file_path}")

                if os.path.exists(file_path):
                    with open(file_path, "rb") as file:
                        files = {"document": file}
                        file_payload = {
                            "chat_id": TELEGRAM_CHAT_ID,
                            "caption": f"📁 *Файл от {jobApplication.name}*",
                            "parse_mode": "Markdown"
                        }
                        file_response = requests.post(
                            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument",
                            data=file_payload, files=files
                        )

                        if file_response.status_code == 200:
                            print("✅ Файл успешно отправлен!")
                        else:
                            print(f"❌ Ошибка при отправке файла: {file_response.text}")
                else:
                    print("⚠️ Файл не найден на сервере!")

        return Response(serializer.errors, status=400)
        return Response(serializer.errors, status=400)

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers

class GalleryView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers

class VideoView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

class Urls_to_social_networkView(generics.ListAPIView):
    queryset = Urls_to_social_network.objects.all() 
    serializer_class = Urls_to_social_networkSerializers


class FileUploadView(APIView):
    def get(self, request, *args, **kwargs):
        files = UploadedFile.objects.all()
        serializer = FileUploadSerializer(files, many=True)
        return Response(serializer.data)