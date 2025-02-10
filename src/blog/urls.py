from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, home

router = DefaultRouter()
router.register(r"comment/", CommentViewSet)


urlpatterns = [path("", home)]
urlpatterns += router.urls
