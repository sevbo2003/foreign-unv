# Generated by Django 4.0.2 on 2022-02-13 11:52

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Davlat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('davlat', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Fanlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fan', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universitet', models.TextField()),
                ('qisqa_nomi', models.CharField(blank=True, max_length=7, null=True)),
                ('about', models.TextField()),
                ('location', models.CharField(max_length=25)),
                ('website', models.URLField()),
                ('requirements', ckeditor.fields.RichTextField()),
                ('hujjatlar', ckeditor.fields.RichTextField()),
                ('imtihon_sanasi', models.DateField()),
                ('sponsor', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='univer_images')),
                ('body', ckeditor.fields.RichTextField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.category')),
                ('davlat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.davlat')),
                ('imtihon_fanlari', models.ManyToManyField(to='university.Fanlar')),
                ('tags', models.ManyToManyField(to='university.Tags')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
