# from django.urls import path, include
from rest_framework.routers import SimpleRouter
router = SimpleRouter()

urlpatterns = router.urls
#
# # urlpatterns = [
#     # path('github/login', GitHubLogin.as_view()),
#     # path('facebook/login', FacebookLogin.as_view()),
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
