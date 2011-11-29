from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pazari.views',
	url(r'^$', 'home'),
)