from django.contrib import admin
from django import forms
from navis.models import Consultation, Services, AboutUs, Tools, Projects, Reviews, Vacancy, JobApplication, \
    Event, Contacts, Gallery, Video, Urls_to_social_network, UploadedFile
from ckeditor_uploader.widgets import CKEditorUploadingWidget


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    model = Consultation
    list_display = ('name', 'phone_number', 'message', 'email')


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
    list_displey = [
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
                "fields": [ "updated_at","baner", "titletwo","description"],
            },
        ),
    ]

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_displey = [
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
    list_display = ('image', 'title', 'language')


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('image', 'first_name', 'last_name', 'job_title', 'title', 'is_active', 'language')

    fieldsets = (
        ("Основная информация", {
            'fields': ('first_name', 'last_name', 'job_title')
        }),
        ("Дополнительно", {
            'fields': ('image', 'title', 'is_active', 'language'),
            'classes': ('collapse',) 
        }),
    )


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
    model = JobApplication
    list_display = ('name', 'phone_number', 'email', 'urls', 'fields')


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
    list_displey = [
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
    list_displey = ('language', 'name', 'phone_number', 'interested', 'date', 'time', 'location', 'slug')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    fields = ('language', 'img')
    list_display = ('language', 'img')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('urls',)

@admin.register(Urls_to_social_network)
class Urls_to_social_network(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_social',)}
    list_displey = ("name_social" , "urls", "logo", "slug")


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at', 'file_type')
    list_filter = ('file_type',)
    search_fields = ('file',)