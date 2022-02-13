from django.shortcuts import render, get_object_or_404
from .models import University, Category, Tags


def university_list(request):
    universities = University.objects.all()
    sponsors = University.objects.filter(sponsor=True)
    categories = Category.objects.all()
    tags = Tags.objects.all()
    context = {
        'univers': universities,
        'sponsors': sponsors,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'home.html', context)