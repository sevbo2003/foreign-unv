from django.db import models
from ckeditor.fields import RichTextField


class Fanlar(models.Model):
    fan = models.CharField(max_length=25)

    def __str__(self):
        return self.fan


class Davlat(models.Model):
    davlat = models.CharField(max_length=25)

    def __str__(self):
        return self.davlat


class Category(models.Model):
    category = models.CharField(max_length=25)

    def __str__(self):
        return self.category


class Tags(models.Model):
    tag = models.CharField(max_length=25)

    def __str__(self):
        return self.tag


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class University(models.Model):
    universitet = models.TextField()
    qisqa_nomi = models.CharField(max_length=7, null=True, blank=True)
    about = models.TextField()
    location = models.CharField(max_length=25)
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tags)
    website = models.URLField()
    requirements = RichTextField()
    hujjatlar = RichTextField()
    imtihon_sanasi = models.DateField()
    imtihon_fanlari = models.ManyToManyField(Fanlar)
    sponsor = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='univer_images')
    body = RichTextField()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.qisqa_nomi
