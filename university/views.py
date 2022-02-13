from django.shortcuts import render, get_object_or_404
from .models import University, Category, Tags
from django.db.models import Q


def university_list(request):
    search_univer = request.GET.get('search')
    if search_univer:
        universities = University.objects.filter(Q(universitet__icontains=search_univer) & Q(about__icontains=search_univer))
    else:
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