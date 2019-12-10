from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import successView

urlpatterns = [
    path('',views.homepage ,name='homepage'),
    path('about/',views.about ,name='about'),
    path('service/',views.service ,name='service'),
    path('contact/',views.contact ,name='contact'),
    # path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]
