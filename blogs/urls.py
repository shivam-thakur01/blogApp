from django.urls import path
from .views import home
from .views import post,category

urlpatterns = [
    path('blogs/',home),
    path('blogs/<slug:url>',post),
    path('category/<slug:url>',category),
]
