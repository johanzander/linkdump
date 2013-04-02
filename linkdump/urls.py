from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linkdump.views.home', name='home'),
    # url(r'^linkdump/', include('linkdump.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^links/$', 'linkdump.linktracker.views.list'),

    url(r'^links/(?P<page>\d+)', 'linkdump.linktracker.views.list'),

    url(r'^links/new', 'linkdump.linktracker.views.new'),

    url(r'^links/add', 'linkdump.linktracker.views.add'),

    url(r'^links/edit/(?P<id>\d+)', 'linkdump.linktracker.views.edit'),

    url(r'^links/update/(?P<id>\d+)', 'linkdump.linktracker.views.update'),

    url(r'^links/delete/(?P<id>\d+)', 'linkdump.linktracker.views.delete')
)
