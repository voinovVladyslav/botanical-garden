from django.urls import path, include
from rest_framework import routers

from news import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
