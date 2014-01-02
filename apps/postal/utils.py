# encoding: utf-8

# mails the admin after being pm’d

from django.core.mail import send_mail
from smtplib import SMTPException

def mail_moderator(subject, message):
    """
    Mails the moderator after being pm’d
    """
    try:
        from_email = "digitaltextbookstudy@gmail.com"
        moderator_email = "netuserlc@gmail.com"
        send_mail(subject, message, from_email, [moderator_email,])
    except SMTPException:
        print "There was an error sending the email"
    return
