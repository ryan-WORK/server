from __future__ import absolute_import

from functools import wraps

from django.http import HttpRequest

from . import ALL, UNSAFE
from .exceptions import AccountBlocked
from .utils import is_account_blocked


__all__ = ['account_blocked']


def account_blocked(group=None, key=None, rate=None, method=ALL, block=False):
    def decorator(fn):
        @wraps(fn)
        def _wrapped(*args, **kw):
            # Work as a CBV method decorator.
            if isinstance(args[0], HttpRequest):
                request = args[0]
            else:
                request = args[1]
            request.limited = getattr(request, 'limited', False)
            account_is_blocked = is_account_blocked(request=request, group=group, fn=fn,
                                                    key=key, rate=rate, method=method,
                                                    increment=True)
            if account_is_blocked and block:
                #  Throw PermissionDenied from django.core.exceptions import PermissionDenied
                raise AccountBlocked()
            return fn(*args, **kw)
        return _wrapped
    return decorator


account_blocked.ALL = ALL
account_blocked.UNSAFE = UNSAFE