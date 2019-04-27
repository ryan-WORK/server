from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet, ResponseViewSet, ArticleList


app_name = 'health'
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'response', ResponseViewSet)

urlpatterns = [
    path('api/v1/health/', include(router.urls)),
    url('^api/v1/typeof/(?P<typeof>.+)/', ArticleList.as_view(), name="t"),

]
