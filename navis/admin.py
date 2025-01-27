from django.contrib import admin
from navis.models import Consultation, Services, AboutUs, Tools, Projects, Reviews, Vacancy, JobApplication, \
    Event, Contacts, Gallery


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    model = Consultation
    list_display = ('phone_number', 'email')

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
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
                "fields": ["design", "analysis", "framework", "img_framework" ,"additionUI", "img_additionUI"],
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
    list_display = ('image', 'first_name', 'last_name', 'job_title', 'title', 'language')

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('level','job_title' ,'schedule', 'title','title_work' ,'description', 'responsibilities', 'requirements', 'working_conditions', 'language')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'urls', 'language')

@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
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
                "fields": ["description", "requirements", "date2", "time2"],
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