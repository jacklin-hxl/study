from flask import render_template
from flask_mail import Message

from app import mail


def send_mail(recipient, subject, template, **kwargs):
    msg = Message(subject=subject, recipients=[recipient])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
