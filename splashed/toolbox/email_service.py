from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def o_o_mail(subject_mess, title, body, more, to_who, fromwho, gisting, app_url):

    html_message = render_to_string(
        'splashed/emails/email.html',
        {
            'title': f'[College Budget Studio] {title}',
            'fromwho': f'{fromwho}',
            'body': f"{body}",
            'more': f"{more}",
            'support': f'{gisting}',
            'location_url': f'{app_url}',

        }
    )
    send_mail(subject=subject_mess, message="", from_email=settings.EMAIL_HOST_USER,
              recipient_list=to_who, fail_silently=False, html_message=html_message)

# subject = ''.join(subject.splitlines())
