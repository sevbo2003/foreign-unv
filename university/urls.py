from django.urls import path
from .views import university_list, university_detail

urlpatterns = [
    path('', university_list, name='home'),
    path('<slug:slug>', university_detail, name='detail'),
]