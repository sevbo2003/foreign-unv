from django.shortcuts import render, get_object_or_404, redirect
from .models import University, Category, Tags, Comment
from django.db.models import Q
from django.core.mail import send_mail
from marketing.forms import EmailForm
from marketing.models import Subscribers
from .forms import CommentForm
from datetime import datetime


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


def university_detail(request, slug):
    universitet = get_object_or_404(University, slug=slug)
    sponsors = University.objects.filter(sponsor=True)
    categories = Category.objects.all()
    tags = Tags.objects.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            p = Comment(
                name=name,
                email=email,
                comment=comment,
                univer=universitet,
                created=datetime.now()
            )
            p.save()
            return redirect('detail', universitet.slug)
    else:
        comment_form = CommentForm()
    form = EmailForm()
    context = {
        'univer': universitet,
        'sponsors': sponsors,
        'categories': categories,
        'tags': tags,
        'comment_form': form,
        'form': form
    }
    return render(request, 'detail_page.html', context)