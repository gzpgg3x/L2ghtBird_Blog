from django.conf.urls import patterns, include, url
# from blog.views import main

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'dbe.views.home', name='home'),
#     # url(r'^dbe/', include('dbe.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),

# )

urlpatterns = patterns('blog.views',
    url(r'^admin/', include(admin.site.urls)),
    # (r'^$', "main"),
    # (r"^(\d-)/$", "post"),
    url(r'^', 'main'),
    url(r'^(\d-)/$', 'post'),
    url(r'^add_comment/(\d+)/$', 'add_comment'), 
    # (r"^add_comment/(\d+)/$", "add_comment"),   
)
