from rest_framework import serializers
from blog.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# class UserCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserComment
#         fields = '__all__'
