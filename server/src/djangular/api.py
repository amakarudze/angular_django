from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import VideoSerializer
from .models import Video


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = (permissions.IsAuthenticated,)
