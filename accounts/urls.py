# accounts/urls.py

# from django.urls import path, include
from rest_framework.routers import SimpleRouter

# from .views import ReturnAuthCode, GetUserProfile
# from .views import UserViewSet, PostViewSet, GitHubLogin, FacebookLogin, UserProfileViewSet, Posting

# from accounts.views import LoginView

router = SimpleRouter()
# router.register('users', UserViewSet, base_name='users')
# router.register('matches', UserViewSet, base_name='new-users')

urlpatterns = router.urls

urlpatterns += [
    # path('login/', LoginView.as_view(), name='login'),
    # path('github/login', GitHubLogin.as_view()),
    # path('facebook/login', FacebookLogin.as_view()),
    # path('facebook/login', P.as_view()),
]
#
# from django.urls import path, include
# from . import views
#
# # urlpatterns = [
#
#     # path('signup/', views.SignUp.as_view(), name='signup'),
#     # path('login/', views.LoginView.as_view(), name='login'),
#
#     # path ('password_change/', PasswordChangeView.as_view (), name='password_change'),
#     # path ('password_change/done/', PasswordChangeDoneView.as_view (), name='password_change_done'),
#     #
#     # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
#     # path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
#     # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     # path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# # ]
