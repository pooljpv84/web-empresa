# Generated by Django 3.2.5 on 2021-08-12 02:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_auto_20210811_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
