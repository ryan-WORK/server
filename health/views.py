# from django.core.mail import send_mail
from rest_framework import viewsets, generics
# from .utils.alerts import BlogEmailErrors
from .models import Article, Response
# from django.conf import settings
# from splashed.toolbox.email_service import o_o_mail
from .api.serializers import ResponseSerializer, ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ResponseViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()


class ArticleList(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        article = self.kwargs['typeof']
        return Article.objects.filter(typeof=article)


# class ResponseList(generics.ListAPIView):
#     serializer_class = ResponseSerializer
#
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         article = self.kwargs['typeof']
#         return Article.objects.filter(typeof=article)
