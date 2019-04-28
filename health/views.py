# from django.core.mail import send_mail
from rest_framework import generics
from .models import Article, File, ArticleFile
from .models import Response as UserResponse
# from django.conf import settings
# from splashed.toolbox.email_service import o_o_mail
from .api.serializers import ResponseSerializer, ArticleSerializer, \
    ArticleFileSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .api.serializers import FileSerializer


class ArticleList(generics.ListAPIView):
    """
    Get only search Type of
    """

    permission_classes = ()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        article = self.kwargs['typeof']
        return Article.objects.filter(typeof=article)


class ArticleIDList(generics.ListAPIView):
    """
    Get only search Type of
    """

    permission_classes = ()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        aid = self.kwargs['aid']
        return Article.objects.filter(id=aid)


class FileFinderList(generics.ListAPIView):
    """
    Get only search Type of
    """

    permission_classes = ()
    serializer_class = ArticleFileSerializer

    def get_queryset(self):
        aid = self.kwargs['aid']
        return ArticleFile.objects.filter(article=aid)


class ResponsePost(generics.ListCreateAPIView):
    queryset = UserResponse.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = ()
    '''
    Create Only with token
    '''
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(email=user.email)


class ResponseUserList(generics.ListAPIView):
    """
    Get only search Type of
    """

    permission_classes = ()
    serializer_class = ResponseSerializer

    def get_queryset(self):
        email = self.kwargs['email']
        return UserResponse.objects.filter(email=email)


class FileUploadView(APIView):
    permission_classes = ()
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            # file_serializer.save()
            user = self.request.user
            file_serializer.save(email=user.email)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleFileUploadView(APIView):
#     permission_classes = ()
#     parser_class = (FileUploadParser,)
#
#     def post(self, request, *args, **kwargs):
#
#         file_serializer = ArticleFileSerializer(data=request.data)
#         if file_serializer.is_valid():
#             # file_serializer.save()
#             # user = self.request.user
#             # file_serializer.save(email=user.email)
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResponseFileFinderList(generics.ListAPIView):
    """
    Get only search Type of
    """

    permission_classes = ()
    serializer_class = FileSerializer

    def get_queryset(self):
        rid = self.kwargs['rid']
        return File.objects.filter(response=rid)
