from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
import django.contrib.auth.views

from views import *


urlpatterns = patterns('',

    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),

   # url('^', include('django.contrib.auth.urls')),

    url(r'^password/change/$',
                    auth_views.password_change,
                    name='password_change'),
    url(r'^password/change/done/$',
                    auth_views.password_change_done,
                    name='password_change_done'),
    url(r'^password/reset/$',
                    auth_views.password_reset,
                    name='password_reset'),
    url(r'^accounts/password/reset/done/$',
                    auth_views.password_reset_done,
                    name='password_reset_done'),
    url(r'^password/reset/complete/$',
                    auth_views.password_reset_complete,
                    name='password_reset_complete'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                    auth_views.password_reset_confirm,
                    name='password_reset_confirm'),

    url(r'^$', 'tracker.views.home', name='home'),
    #url(r'^mobilereg/$', 'tracker.views.mobileReg', name='home'),
    url(r'^update_profile/$', update_profile, name='profile'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^track/$', track, name='track'),
    url(r'^mobileReg/$', mobileReg, name='track'),
    url(r'^adduser/$', adduser, name='track'),
    url(r'^add_device/$', adddevice, name='track'),
    url(r'^trackdetails/$', trackdetails, name='track'),
)