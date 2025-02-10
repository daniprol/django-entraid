from django.http import HttpResponse
from rest_framework import generics, viewsets

from .models import Comment
from .serializers import CommentSerializer


def home(request):
    return HttpResponse("Hello world")


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
