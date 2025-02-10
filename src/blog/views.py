from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import generics, viewsets

from .models import Comment
from .serializers import CommentSerializer


def home(request):
    return HttpResponse("Hello world")


@login_required()
def private_view(request):
    return HttpResponse("Private")


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
