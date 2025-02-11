from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Comment
from .serializers import CommentSerializer


def home(request):
    return HttpResponse("Hello world")


# NOTE: login_required() also works
@login_required
def private_view(request):
    return HttpResponse("Private")


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def private_api_view(request):
    return HttpResponse("API private view")


def login_failed(request):
    return HttpResponse("Login failed lol", status_code=403)
