# Generated by Django 4.0.2 on 2022-02-13 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_university_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'author', 'verbose_name_plural': 'Authorlar'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'Categoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='davlat',
            options={'verbose_name': 'davlat', 'verbose_name_plural': 'Davlat'},
        ),
        migrations.AlterModelOptions(
            name='fanlar',
            options={'verbose_name': 'fan', 'verbose_name_plural': 'Fanlar'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'ordering': ('-created',), 'verbose_name': 'Universitet', 'verbose_name_plural': 'Universitetlar'},
        ),
    ]
