from django.urls import path
from .views import university_list, university_detail, category_list, tag_list

urlpatterns = [
    path('', university_list, name='home'),
    path('<slug:slug>', university_detail, name='detail'),
    path('kategoriya/<int:pk>/<str:category>/', category_list, name='cat_list'),
    path('teg/<int:pk>/<str:tag>/', tag_list, name='tag_list'),
]