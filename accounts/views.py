from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from .security_tools.mixins import AccountBlockMixin

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework.permissions import IsAuthenticated

from accounts.api.serializers import UserSerializer
from accounts.models import User


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions --RC.

        Additionally we also provide an extra `highlight` action.
    """
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class LoginView(generic.FormView):
#     form_class = AuthenticationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/login.html"
#
#     def get_form(self, form_class=None):
#         if form_class is None:
#             form_class = self.get_form_class()
#         return form_class(self.request, **self.get_form_kwargs())
#
#     def form_valid(self, form):
#         login(self.request, form.get_user())
#         return super().form_valid(form)


# class LogoutView (generic.RedirectView):
#     url = reverse_lazy("blog:post_list")
#
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return super().get (request, *args, **kwargs)

#
# class SignUp (AccountBlockMixin, generic.CreateView):
#     account_blocked_key = 'ip'
#     account_blocked_rate = '5/m'
#     account_blocked_block = True
#     account_blocked_method = 'GET'
#
#     form_class = UserCreateForm
#     success_url = reverse_lazy ('login')
#     template_name = 'registration/signup.html'
# class ReturnAuthCode(APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#
#     def get(self, request):
#         return Response({'ok': 100})
#
#
# class GetUserProfile(APIView):
#     permission_classes = (IsAdminOrReadOnly,)

# def post(self, request):
#     name = Token.objects.get(key='17d6116c284972b05fa4c8e03b72070b2bc0c02d')
#     # print(name.user, name.user_id)
#     # u = UserProfile.objects.get(user=name.user)
#     # re = UserProfileSerializer(u).data
#
#     return Response({'key': '17d6116c284972b05fa4c8e03b72070b2bc0c02d',
#                      'name': 'o__o'})
#
# def get(self, request):
#     # name = Token.objects.get(key='17d6116c284972b05fa4c8e03b72070b2bc0c02d')
#     # print(name.user, name.user_id)
#     # u = UserProfile.objects.get(user=name.user)
#     # re = UserProfileSerializer(u).data
#
#     return Response({'key': '17d6116c284972b05fa4c8e03b72070b2bc0c02d',
#                      'name': 'o__o',
#                      'email': '',
#                      'passw': 'testadmin123'})
