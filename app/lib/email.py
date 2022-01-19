from threading import Thread

from flask import render_template, current_app
from flask_mail import Message

from app import mail


def asynchronous_send(msg, app):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


# 异步发送
def send_mail(recipient, subject, template, **kwargs):
    msg = Message(subject=subject, recipients=[recipient])
    msg.html = render_template(template, **kwargs)
    worker = Thread(target=asynchronous_send, args=(msg, current_app.app_context().app))
    worker.start()

