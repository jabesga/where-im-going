from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^create-event/$', views.create_event, name="create_event"),
                       url(r'^event/(?P<event_id>\d+)/$', views.event, name="event"),
                       url(r'^event/(?P<event_id>\d+)/join/$', views.join_event, name="join_event"),
                       url(r'^user/(?P<user_name>.[A-Za-z0-9_]+)/$', views.profile, name="profile"),
                       url(r'^user/(?P<user_name>.[A-Za-z0-9_]+)/follow/$', views.follow_user, name="follow_user"),
                       
                       url(r'^homepage$', views.homepage, name="homepage"),
                       url(r'^homepage1$', views.homepage1, name="homepage1"),
                       url(r'^homepage2$', views.homepage2, name="homepage2"),
                       )