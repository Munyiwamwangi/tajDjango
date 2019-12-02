import datetime

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from django.urls import reverse, reverse_lazy
from .email import move_request_email

from .forms import ContactForm

# Create your views here.

def homepage(request):
    todays_date = datetime.datetime.now()
    return render(request, 'index.html',{'todays_date':todays_date})

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            recipient_list = ['jmunyiwamwangi@gmail.com']
            try:
                send_mail(subject, message,from_email,recipient_list, fail_silently='False',auth_user=None, auth_password=None)
            except BadHeaderError:
                return HttpResponse('Please recheck email')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            mail = form.cleaned_data['from_email']

            try:
                move_request_email(name,subject, message, mail)
            except BadHeaderError:
                return HttpResponse('Please input correct details as directed')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message. We will reply shortly,')
