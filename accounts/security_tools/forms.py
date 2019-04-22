from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _


#  Example Auth Form Custom
class AccountsAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            print("is not active")
            raise forms.ValidationError(
                _("This account is inactive."),
                code='inactive',
            )
        # TODO: this is just an example of how this will work ... it needs to be logically applied to each situation
        # if user.username.startswith('r'):
        if user.is_staff:
            print("blocked user", user.username)
            raise forms.ValidationError(
                _("Sorry, accounts starting with 'b' aren't welcome here."),
                code='no_b_users',
            )



