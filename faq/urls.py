from django.conf.urls.defaults import patterns, url

from faq import views

urlpatterns = patterns('',
	url(r'^(?P<slug>[-\w]+)/$',
		view = views.FAQQuestionDetailView.as_view(),
		name = 'faq_question_detail'
	),
	url(r'^$',
		view = views.FAQQuestionListView.as_view(),
		name = 'faq_index',
	),
)