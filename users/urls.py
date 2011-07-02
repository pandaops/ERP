from django.conf.urls.defaults import *
from django.views.generic.simple import *

urlpatterns = patterns('erp.users.views',
      (r'^$', 'handle_profile'),
      (r'^register/?(\w+)?/?(\w+)?/?(\w+)?/$', 'register_user'),
      (r'^invite/$', 'invite'),
      (r'^profile/$', 'handle_profile'),
      #(r'^search/', include('haystack.urls')),
)
#      (r'^department/?(\w+)?$', 'display_department_portal'),
