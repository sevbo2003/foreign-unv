from django.contrib import admin
from .models import Davlat, Category, Tags, Author, Fanlar, University

admin.site.register(Davlat)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Author)
admin.site.register(Fanlar)


@admin.register(University)
class UniverAdmin(admin.ModelAdmin):
    list_display = ('qisqa_nomi', 'location', 'davlat', 'author',
                    'website', 'category', 'imtihon_sanasi', 'sponsor')
    search_fields = ('qisqa_nomi', 'universitet', 'location', 'davlat', 'author',
                     'website', 'category',)
    list_filter = ('author', 'davlat', 'location',)
    prepopulated_fields = {'slug': ('universitet',)}
