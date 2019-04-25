from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import post_detail, post_list, post_search, post_share, PostsViewSet, app_about
from .feeds import LatestPostsFeed


app_name = 'blog'
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'remote', PostsViewSet)
urlpatterns = [
    path('api/v1/blog/', include(router.urls)),
    # post views
    # path('about-me/', app_about, name='app_about'),
    # path('', post_list, name='post_list'),
    # # path('', PostListView.as_view(), name='post_list'),
    # path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    #      post_detail,
    #      name='post_detail'),
    # path('<int:post_id>/share/',
    #      post_share, name='post_share'),
    # path('tag/<slug:tag_slug>/',
    #      post_list, name='post_list_by_tag'),
    # path('feed/', LatestPostsFeed(), name='post_feed'),
    # path('search/', post_search, name='post_search'),

]
