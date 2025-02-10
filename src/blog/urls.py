from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, home, private_view

router = DefaultRouter()
router.register(r"comment/", CommentViewSet)


urlpatterns = [path("", home), path("private/", private_view)]
urlpatterns += router.urls
