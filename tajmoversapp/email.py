from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def move_request_email(name,subject,message,receiver):
    sender = 'jmunyiwamwangi@gmal.com'

    text_content = render_to_string('email/moverequest.txt',{"name": name, "subject":subject, "message":message})
    html_content = render_to_string('email/moverequest.html',{"name":name, "subject":subject, "message":message})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()