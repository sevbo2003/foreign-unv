from django.shortcuts import render


def university_list(request):
    return render(request, 'home.html')