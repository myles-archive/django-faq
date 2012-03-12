from django.conf.urls.defaults import patterns, url

from faq import views

urlpatterns = patterns('',
	url(r'^category/(?P<slug>[-\w]+)/$',
		view = views.FAQCategoryDetailView.as_view(),
		name = 'faq_category_detail'
	),
	url(r'^category/$',
		view = views.FAQCategoryListView.as_view(),
		name = 'faq_category_list'
	),
	url(r'^(?P<slug>[-\w]+)/$',
		view = views.FAQQuestionDetailView.as_view(),
		name = 'faq_question_detail'
	),
	url(r'^$',
		view = views.FAQQuestionListView.as_view(),
		name = 'faq_question_list',
	),
)