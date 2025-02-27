# Generated by Django 5.1.2 on 2025-02-22 07:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Russian', 'Rus'), ('English', 'ENG')], max_length=10)),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('description', models.CharField(max_length=255, verbose_name='Подробная информация')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='@Email')),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Консультация',
                'verbose_name_plural': 'Консультация',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Russian', 'Rus'), ('English', 'ENG')], max_length=255)),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone_number', models.IntegerField(verbose_name='Номер телефона')),
                ('interested', models.CharField(max_length=255, verbose_name='Что вас интересует')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('location', models.CharField(max_length=255, verbose_name='Место встречи')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакт',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Russian', 'Rus'), ('English', 'ENG')], max_length=10)),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('topic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тема')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата добавление')),
                ('time', models.TimeField(verbose_name='Время добавление')),
                ('location', models.CharField(max_length=255, verbose_name='Местоположение')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date2', models.DateField(verbose_name='Дата добавление 2')),
                ('time2', models.TimeField(verbose_name='Время добавление 2')),
            ],
            options={
                'verbose_name': 'Мероприятия',
                'verbose_name_plural': 'Мероприятии',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Russian', 'Rus'), ('English', 'ENG')], max_length=10)),
                ('img', models.ImageField(upload_to='gallery_images/')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер')),
                ('email', models.EmailField(max_length=100, verbose_name='@Email')),
                ('urls', models.URLField(blank=True, null=True, verbose_name='Ссылка на соцсеть')),
                ('fields', models.FileField(blank=True, null=True, upload_to='job_application', verbose_name='Прикрепите файл')),
            ],
            options={
                'verbose_name': 'Заявление о приеме на работу',
                'verbose_name_plural': 'Заявление о приеме на работу',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Russian', 'Rus'), ('English', 'ENG')], max_length=10)),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Проекты',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Russian', 'Rus'), ('English', 'ENG')], max_length=10)),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=255, verbose_name='Должность')),
                ('title', models.CharField(max_length=1000, verbose_name='Информация')),
                ('is_active', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Russian', 'Rus'), ('English', 'ENG')], max_length=10)),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('sphere', models.CharField(max_length=255, verbose_name='Сфера')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('industry', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Отрасль')),
                ('baner', models.ImageField(upload_to='', verbose_name='Банер')),
                ('titletwo', models.CharField(max_length=255, verbose_name='Описание 2')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('updated_at', models.DateTimeField(verbose_name='Время добавление')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Наши услуги',
                'verbose_name_plural': 'Наши услуги',
            },
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Russian', 'Rus'), ('English', 'ENG')], max_length=10)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Инструменты',
                'verbose_name_plural': 'Инструменты',
            },
        ),
        migrations.CreateModel(
            name='Urls_to_social_network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='', verbose_name='Фото')),
                ('urls', models.URLField(blank=True, null=True, verbose_name='Ссылка на соцсеть')),
                ('name_social', models.CharField(blank=True, null=True, verbose_name='Название соц сети')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Ссылки на соц сети Navis Devs',
                'verbose_name_plural': 'Ссылки на соц сети Navis Devs',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Russian', 'Rus'), ('English', 'ENG')], max_length=10)),
                ('level', models.CharField(choices=[('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior'), ('test', 'test')], max_length=255, verbose_name='Уровень')),
                ('job_title', models.CharField(choices=[('Backend', 'Backend'), ('Frontend', 'Frontend'), ('Fullstack', 'Fullstack'), ('test', 'test')], max_length=255, verbose_name='Должность')),
                ('schedule', models.CharField(choices=[('Полный рабочий день', 'Полный рабочий день'), ('Удаленно', 'Удаленно'), ('Гибридный график', 'Гибридный график')], max_length=255, verbose_name='График')),
                ('title_work', models.CharField(max_length=255, verbose_name='Описание работы')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Слаг')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.URLField(verbose_name='Видeo')),
            ],
            options={
                'verbose_name': 'Видeo',
                'verbose_name_plural': 'Видeo',
            },
        ),
    ]
