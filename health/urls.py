from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from health.views.admin_views import ArticleViewSet
from health.views.user_views import ArticleList, ResponsePost, FileUploadView, \
   FileFinderList, ArticleIDList, ResponseFileFinderList, ResponseUserListGet  # , ResponseUserList

# from .views import ArticleViewSet, ResponseViewSet, ArticleList, ResponsePost, FileUploadView, FileViewSet, \
#     ResponseUserList, FileFinderList, ArticleFileViewSet, ArticleIDList, ResponseFileFinderList

app_name = 'health'
# Create a router and register our viewsets with it.
router = DefaultRouter()
# Developer URLS
router.register(r'articles', ArticleViewSet)
# router.register(r'response', ResponseViewSet)
# router.register(r'file', FileViewSet)
# router.register(r'afile', ArticleFileViewSet)


urlpatterns = [
    # admin
    path('api/v1/staff/', include(router.urls)),
    # Article list for type of article
    url('^api/v1/typeof/(?P<typeof>.+)/', ArticleList.as_view(), name="typeof"),
    # Get Article By ID
    url('^api/v1/article_id/(?P<aid>.+)/', ArticleIDList.as_view(), name="aid"),
    # Post a response or comment to Article of given id
    url('^api/v1/give-response/', ResponsePost.as_view(), name="response"),
    # List Of User Responses by Email
    url('^api/v1/response-user-all/(?P<email>.+)/', ResponseUserListGet.as_view(), name="all-user-response"),
    # url('^api/v1/response-user-all/(?P<email>.+)/', ResponseUserList.as_view(), name="all-user-response"),
    # Upload Photo to Response given By user
    url('^api/v1/file_upload_response/', FileUploadView.as_view(), name="upload"),
    # Find all photos associated with given article ID
    url('^api/v1/file-finder/(?P<aid>.+)/', FileFinderList.as_view(), name="file-finder"),
    # Find all photos associated with given Response ID
    url('^api/v1/response-file-finder/(?P<rid>.+)/', ResponseFileFinderList.as_view(), name="response-file-finder"),
]
