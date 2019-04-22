from django.core.exceptions import PermissionDenied


class AccountBlocked(PermissionDenied):
    def __init__(self):
        Exception.__init__(self, "well, that rather badly didn't it?")
