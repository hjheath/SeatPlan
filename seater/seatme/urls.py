from django.conf.urls import patterns, url

from seatme import views

urlpatterns = patterns(
    '',
    url(r'home/$', views.get_name, name='index'),
    url(r'clear/$', views.clear, name='clear'),
)
