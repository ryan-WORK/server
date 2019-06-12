# from django.core.mail import send_mail
from rest_framework import generics
from health.models import Article, File, ArticleFile
from health.models import Response as UserResponse
# from django.conf import settings
# from splashed.toolbox.email_service import o_o_mail
from health.api.serializers import ResponseSerializer, ArticleSerializer, \
    ArticleFileSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from health.api.serializers import FileSerializer

from rest_framework.permissions import IsAuthenticated


class ArticleList(generics.ListAPIView):
    """
    Get only search Type of
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer

    def get_queryset(self):
        article = self.kwargs['typeof']
        return Article.objects.filter(typeof=article)


class ArticleIDList(generics.ListAPIView):
    """
    Get only search Type of
    """
    # IsAuthenticated
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer

    def get_queryset(self):
        aid = self.kwargs['aid']
        return Article.objects.filter(id=aid)


class FileFinderList(generics.ListAPIView):
    """
    Get only search Type of
    """
    # IsAuthenticated,
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleFileSerializer

    def get_queryset(self):
        aid = self.kwargs['aid']
        return ArticleFile.objects.filter(article=aid)


# IsAuthenticated,
class ResponsePost(generics.ListCreateAPIView):
    queryset = UserResponse.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = (IsAuthenticated,)
    '''
    Create Only with token
    '''
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(email=user.email)


class ResponseUserListGet(generics.ListAPIView):
    """
    Get only search Type of
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ResponseSerializer

    def get_queryset(self):
        user = self.request.user
        print(user.email, self.request)
        return UserResponse.objects.filter(email=user.email)


class ResponseUserListGetUpload(generics.ListAPIView):
    """
    Get only search Type of
    """

    permission_classes = ()
    serializer_class = FileSerializer

    def get_queryset(self):
        user = self.request.user
        print(user.email)
        return File.objects.filter(email=user.email)


# IsAuthenticated,
class FileUploadView(APIView):
    permission_classes = (IsAuthenticated,)
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

# IsAuthenticated,
class ResponseFileFinderList(generics.ListAPIView):
    """
    Get only search Type of
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = FileSerializer

    def get_queryset(self):
        rid = self.kwargs['rid']
        return File.objects.filter(response=rid)
