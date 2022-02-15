from .models import University, Category, Tags


def sponsors(request):
    return {
        'sponsors': University.objects.filter(sponsor=True),
    }


def categories(request):
    return {
        'categories': Category.objects.all(),
    }


def tags(request):
    return {
        'tags': Tags.objects.all()
    }