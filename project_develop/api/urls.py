from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('user/', include(router.urls))
]