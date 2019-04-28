from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


# class ProfileSerializer(serializers.Serializer):
#     profile = serializers.SerializerMethodField()
#
#     def get_profile(self, obj):
#         print(obj)
#         return f"{obj['key']} world"



