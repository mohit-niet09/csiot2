from django.core.mail import send_mail
from django.conf import settings

def send_email_util(subject, body, recipient_list):
    subject = subject
    body = body
    recipient_list = recipient_list
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, body, from_email, recipient_list)