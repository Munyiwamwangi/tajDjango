from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def move_request_email(name,subject,message,receiver):
    sender = 'jmunyiwamwangi@gmail.com'

    text_content = render_to_string('email/moverequest.txt',{"name": name, "message":message, "subject":subject})
    html_content = render_to_string('email/moverequest.html',{"name":name, "message":message, "subject":subject})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    # msg.attach('Attachment.pdf', file_to_be_sent, 'file/pdf')
    msg.attach_alternative(html_content,'text/html')
    msg.send()