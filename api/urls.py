from django.urls import path
from . import views
urlpatterns = [
    path('', views.NewsView.as_view()),
    path('api/migration', views.migration),
]