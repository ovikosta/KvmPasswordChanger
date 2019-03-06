from django.conf.urls import url

from . import views


app_name = 'kvmcp'
urlpatterns = [
    url(r'^$', views.change_page, name='change_page'),
    url(r'activate/$', views.activate, name='activate'),
    url(r'timestamp/$', views.timestamp, name='timestamp'),
    url(r'report/$', views.report, name='report'),
    url(r'checkstatus/$', views.check_status, name='check_status')
]