from django.contrib.sitemaps import Sitemap

from faq.models import Question, Category

class FAQQuestionSitemap(Sitemap):
	changefreq = "never"
	priority = 1.0
	
	def items(self):
		return Question.objects.all()
	
	def lastmod(self, obj):
		return obj.date_modified

class FAQCategorySitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.1
	
	def items(self):
		return Category.objects.all()
	
	def lastmod(self, obj):
		try:
			post = obj.question_set.all()[0]
		except IndexError:
			return None
		return post.date_modified
	
	def location(self, obj):
		return obj.get_absolute_url()