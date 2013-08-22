from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^add/', 'app.views.add', name='add'),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )