from django.contrib import admin
from django import forms
from navis.models import Consultation, Services, AboutUs, Tools, Projects, Reviews, Vacancy, JobApplication, \
    Event, Contacts, Gallery, Video
from ckeditor_uploader.widgets import CKEditorUploadingWidget


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    model = Consultation
    list_display = ('language', 'phone_number', 'email', 'message')


class ServicesAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Services
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = ServicesAdminForm


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    prepopulated_fields = {'slug': ('sphere',)}
    fieldsets = [
        (
            "General info",
            {
                "fields": ["image", "sphere", "title", "industry", "language", "slug"],
            },
        ),
        (
            "Services Detail",
            {
                "classes": ["collapse"],
                "fields": [ "updated_at", "description",],
            },
        ),
    ]

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        (
            "AboutUs",
            {
                "fields": ["title", "image", "language", "slug"],
            },
        ),
        (
            "About us detail",
            {
                "classes": ["collapse"],
                "fields": ["description"],
            },
        ),
    ]


@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    model = Tools
    list_display = ('name', 'image', 'language')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('image', 'title', 'language')

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('image', 'first_name', 'last_name', 'job_title', 'title','is_active' ,'language')


class VacancyAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Vacancy
        fields = '__all__'

class VacancyAdmin(admin.ModelAdmin):
    form = VacancyAdminForm



@admin.register(Vacancy)
class Vacancy(admin.ModelAdmin):
    list_display = ['id', ]
    prepopulated_fields = {'slug': ('title',)}

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'urls', 'language')


class EventAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Event
        fields = '__all__'

class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    forms = VacancyAdminForm
    fieldsets = [
        (
            "Events",
            {
                "fields": ["topic","title", "image", "date", "time", "location", "language"],
            },
        ),
        (
            "Events Detail",
            {
                "classes": ["collapse"],
                "fields": ["date2", "time2", "description"],
            },
        ),
    ]

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ('language', 'name', 'phone_number', 'interested', 'date', 'time', 'location', 'slug')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    fields = ('language', 'img')
    list_display = ('language', 'img')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('urls',)