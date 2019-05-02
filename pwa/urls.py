from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.conf.urls.static import static

admin.site.site_header = 'Wellness Information Network'
admin.site.index_title = 'WIN'                 # default: "Site administration"
admin.site.site_title = 'ADMIN'

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # My Apps
    path('', include('health.urls')),  # list all
    path('accounts/', include('accounts.urls')),  # list all
    path('accounts/', include('django.contrib.auth.urls')),
    # Authorization
    url(r'^api-token-refresh/', refresh_jwt_token, name='api-token-refresh'),
    url(r'^api-token-verify/', verify_jwt_token, name='api-token-verify'),
    path('api-token-auth/', obtain_jwt_token, name='api_token_auth'),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
]
# path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
#      name='django.contrib.sitemaps.views.sitemap'),
# 97746f911b409a254784bbff47ca2c73fa14ea77

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

