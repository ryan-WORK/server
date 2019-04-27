"""pwa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_auth import registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    # Helper URLs

    # My Apps
    path('', include('health.urls')),  # list all
    path('accounts/', include('accounts.urls')),  # list all
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
# path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
#      name='django.contrib.sitemaps.views.sitemap'),
# 97746f911b409a254784bbff47ca2c73fa14ea77
# path('api-auth/', include('rest_framework.urls')), # DRF default
