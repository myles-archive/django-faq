from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

from faq.sitemaps import FAQQuestionSitemap, FAQCategorySitemap

admin.autodiscover()

sitemaps = {
	'faq': FAQQuestionSitemap,
	'faq-category': FAQCategorySitemap
}

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	
	url(r'^faq/', include('faq.urls')),
	
	url(r'^sitemap.xml$',
		'django.contrib.sitemaps.views.sitemap',
		{ 'sitemaps': sitemaps },
		name = 'sitemap'
	),
)
