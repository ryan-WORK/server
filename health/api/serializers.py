from rest_framework import serializers
from health.models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ResponseSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('id', 'name', 'body', 'article')


class AllFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('response', 'file', 'created', 'updated',)


class ArticleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleFile
        fields = "__all__"

