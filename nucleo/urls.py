from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^uploads/$', UploadView.as_view()),
    url(r'^index/$', MinhaView.as_view()),
]
