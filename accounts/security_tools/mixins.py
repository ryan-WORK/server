from __future__ import absolute_import

from . import ALL, UNSAFE
from .decorators import account_blocked


__all__ = ['AccountBlockMixin']


class AccountBlockMixin(object):
    """
    Mixin for usage in Class Based Views
    configured with the decorator ``security_tools`` defaults.

    Configure the class-attributes prefixed with ``account_blocked_``
    for customization of the security_tools process.

    Example::

        class ContactView(AccountBlockMixin, FormView):
            form_class = ContactForm
            template_name = "contact.html"

            # Limit contact form by remote address.
            account_blocked_key = 'ip'
            account_blocked_block = True

            def form_valid(self, form):
                # Whatever validation.
                return super(ContactView, self).form_valid(form)

    """
    account_blocked_group = None
    account_blocked_key = None
    account_blocked_rate = '5/m'
    account_blocked_block = False
    account_blocked_method = ALL

    ALL = ALL
    UNSAFE = UNSAFE

    def get_account_blocked_config(self):
        # Ensures that the account_blocked_key is called as a function instead
        # of a method if it is a callable (ie self is not passed).
        if callable(self.account_blocked_key):
            self.account_blocked_key = self.account_blocked_key.__func__
        return dict(
            group=self.account_blocked_group,
            key=self.account_blocked_key,
            rate=self.account_blocked_rate,
            block=self.account_blocked_block,
            method=self.account_blocked_method,
        )

    def dispatch(self, *args, **kwargs):
        return account_blocked(
            **self.get_account_blocked_config()
        )(super(AccountBlockMixin, self).dispatch)(*args, **kwargs)
