from datetime import timezone, timedelta, datetime
from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import pytz


class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted')

        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        Token
        if token.created < utc_now - settings.TOKEN_EXPIRE_TIME:
            raise AuthenticationFailed('Token has expired')

        return token.user, token


def is_token_expired(token):
    min_age = timezone.now() - timedelta(
        seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS)
    expired = token.created < min_age
    return expired


class ExpiringTokenAuthenticationX(TokenAuthentication):
    """Same as in DRF, but also handle Token expiration.

    An expired Token will be removed and a new Token with a different
    key is created that the User can obtain by logging in with his
    credentials.

    Raise AuthenticationFailed as needed, which translates
    to a 401 status code automatically.
    https://stackoverflow.com/questions/14567586
    """
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid token")

        if not token.user.is_active:
            raise AuthenticationFailed("User inactive or deleted")

        expired = is_token_expired(token)
        if expired:
            token.delete()
            Token.objects.create(user=token.user)
            raise AuthenticationFailed("Token has expired")

        return (token.user, token)
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'myproject.authentication.ExpiringTokenAuthentication',
#     )
# }

# import datetime
# TOKEN_EXPIRE_TIME=datetime.timedelta(days=30)
