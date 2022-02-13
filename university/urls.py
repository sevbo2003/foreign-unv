from django.urls import path
from .views import university_list

urlpatterns = [
    path('', university_list, name='home'),
]