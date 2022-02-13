from django.shortcuts import render, get_object_or_404, redirect
from .models import University, Category, Tags
from django.db.models import Q
from django.core.mail import send_mail
from marketing.forms import EmailForm
from marketing.models import Subscribers


def university_list(request):
    search_univer = request.GET.get('search')
    if search_univer:
        universities = University.objects.filter(Q(universitet__icontains=search_univer) & Q(about__icontains=search_univer))
    else:
        universities = University.objects.all()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            p = Subscribers(email=email)
            p.save()
            send_mail('Xush kelibsiz', 'Siz email xabarnomaga muvaffaqiyatli a\'zo bo\'ldingiz. Rahmat :)', 'sevbofx@gmail.com', (email,))
            redirect('home')
    else:
        form = EmailForm()
    sponsors = University.objects.filter(sponsor=True)
    categories = Category.objects.all()
    tags = Tags.objects.all()
    context = {
        'univers': universities,
        'sponsors': sponsors,
        'categories': categories,
        'tags': tags,
        'form': form
    }
    return render(request, 'home.html', context)