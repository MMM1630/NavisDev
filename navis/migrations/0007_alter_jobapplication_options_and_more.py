# Generated by Django 5.1.2 on 2025-02-26 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navis', '0006_alter_aboutus_language_alter_contacts_language_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobapplication',
            options={'verbose_name': 'Заявление о приеме на работу', 'verbose_name_plural': 'Заявления о приеме на работу'},
        ),
        migrations.RenameField(
            model_name='jobapplication',
            old_name='fields',
            new_name='file',
        ),
    ]
