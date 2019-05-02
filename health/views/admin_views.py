from rest_framework import viewsets
from health.models import Response as UserResponse, File, ArticleFile, Article
from health.api.serializers import ResponseSerializerAll, ArticleSerializer, AllFileSerializer, ArticleFileSerializer
from rest_framework.permissions import IsAdminUser


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    # permission_classes = ()
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class FileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AllFileSerializer
    queryset = File.objects.all()


class ArticleFileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleFileSerializer
    queryset = ArticleFile.objects.all()


class ResponseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ResponseSerializerAll
    queryset = UserResponse.objects.all()
