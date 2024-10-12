from django.urls import path
from .views import HomePageView, CvPageView

urlpatterns = [
    path('',HomePageView.as_view(), name='index'),
     path('cv/', CvPageView.as_view(), name='cv'),
]
