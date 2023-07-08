# Generated by Django 4.2.2 on 2023-06-30 10:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('school', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('pro_phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('pro_email', models.EmailField(max_length=255)),
                ('address', models.CharField(max_length=500)),
                ('pro_address', models.CharField(max_length=500)),
                ('birthday', models.CharField(max_length=255)),
                ('image', models.ImageField(default='', upload_to='images/')),
                ('profil_image', models.ImageField(default='', upload_to='images/')),
                ('about_me', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_class', models.CharField(max_length=255)),
                ('service', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255)),
                ('tag_color', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('image', models.ImageField(default='', upload_to='images/')),
                ('tech_used', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
            ],
        ),
    ]
