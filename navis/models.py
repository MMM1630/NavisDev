from tkinter.constants import CASCADE

from django.db import models
from django.db.models import IntegerField, ForeignKey
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from navis.choices import STATUS_CHOICES, SCHEDULE_CHOICES, LANGUAGE_CHOICES, JOB_TITLE_CHOICES
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Consultation(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    phone_number = models.CharField(_('Номер телефона'), max_length=20, default='+996')
    email = models.EmailField(_('@Email'), max_length=50)

    class Meta:
        verbose_name = "Консультация"
        verbose_name_plural = "Консультация"

    def __str__(self):
        return f"консультация на номере {self.phone_number} еме-йл {self.email}"

class Services(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    image = models.ImageField('Фото')
    sphere = models.CharField('Сфера', max_length=255)
    title = models.CharField('Описание', max_length=255)
    industry = RichTextUploadingField('Отрасль', config_name='default')
    description = RichTextUploadingField(config_name='default')
    updated_at = models.DateTimeField('Время добавление')
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Наши услуги'
        verbose_name_plural = 'Наши услуги'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.sphere)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        if self.slug:
            return reverse('service_detail', kwargs={'slug': self.slug})
        return "/"

class AboutUs(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    title = models.CharField('Описание', max_length=255)
    image = models.ImageField('Фото')
    description = models.CharField('Подробная информация', max_length=255)
    slug = models.SlugField("Слаг", max_length=255, null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('about_us_detail', kwargs={'slug': self.slug})

class Gallery(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    img = models.ImageField(upload_to='gallery_images/')  # Поле для изображения

    verbose_name = 'Галерея'
    class Meta:
        verbose_name_plural = 'Галерея'

class Tools(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    name = models.CharField('Название', max_length=255)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Инструменты'
        verbose_name_plural = 'Инструменты'

    def __str__(self):
        return self.name


class Projects(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    image = models.ImageField('Фото')
    title = models.CharField('Описание', max_length=255)
    slug = models.SlugField("Слаг", max_length=255, null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Reviews(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    image = models.ImageField('Фото')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField('Должность', max_length=255)
    title = models.CharField('Информация',max_length=1000)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField("Слаг", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Vacancy(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    level = models.CharField('Уровень', max_length=255, choices=STATUS_CHOICES)
    job_title = models.CharField('Должность', max_length=255, choices=JOB_TITLE_CHOICES)
    schedule = models.CharField('График', max_length=255, choices=SCHEDULE_CHOICES)
    title = models.CharField('Описание', max_length=255)
    slug = models.SlugField("Слаг", max_length=255, null=True, blank=True, unique=True)
    content = RichTextUploadingField(config_name='default')


    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class JobApplication(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    name = models.CharField('Имя', max_length=255)
    phone_number = models.IntegerField('Номер', default='+996')
    email = models.EmailField('@Email', max_length=100)
    urls = models.URLField('Ссылка на соцсеть')

    class Meta:
        verbose_name = 'Заявление о приеме на работу'
        verbose_name_plural = 'Заявление о приеме на работу'

    def __str__(self):
        return self.name

class Event(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    image = models.ImageField('Фото')
    topic = models.CharField('Тема', max_length=255, null=True, blank=True)
    title = models.CharField('Описание', max_length=255)
    date = models.DateField('Дата добавление')
    time = models.TimeField('Время добавление')
    location = models.CharField('Местоположение', max_length=255)
    description = RichTextUploadingField(config_name='default')
    date2 = models.DateField('Дата добавление 2')
    time2 = models.TimeField('Время добавление 2')

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятии'

class Contacts(models.Model):
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=255)
    name = models.CharField('Имя', max_length=255)
    phone_number = IntegerField('Номер телефона', default='+996')
    interested =  models.CharField('Что вас интересует', max_length=255)
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    location = models.CharField('Место встречи', max_length=255)
    slug = models.SlugField("Слаг", max_length=255, null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакт'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='Проекты')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name='Вакансии')
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, verbose_name='О нас')
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE, verbose_name='Отзывы')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

class Video(models.Model):
    urls = models.URLField('Видeo')

    class Meta:
        verbose_name = 'Видeo'
        verbose_name_plural = 'Видeo'