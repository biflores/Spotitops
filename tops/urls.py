# tops/urls.py
from django.urls import path
from tops import views

urlpatterns = [
    path("", views.HomePageView.as_view()),
    path("about/", views.AboutPageView.as_view())
]