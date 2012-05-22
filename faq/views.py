from django.http import Http404
from django.views.generic import ListView, DetailView

from faq.models import Question, Category

class FAQQuestionListView(ListView):
	
	context_object_name = "question_list"
	template_name = "faq/question_list.html"
	
	def get_queryset(self):
		return Question.objects.filter(categories=None)

class FAQQuestionDetailView(DetailView):
	
	context_object_name = 'question'
	template_name = 'faq/question_detail.html'
	
	def get_object(self):
		return Question.objects.get(slug__iexact=self.kwargs['slug'])

class FAQCategoryListView(ListView):
	
	context_object_name = "category_list"
	template_name = "faq/category_list.html"
	
	def get_queryset(self):
		return Category.objects.all()

class FAQCategoryDetailView(ListView):
	
	context_object_name = 'question_list'
	template_name = "faq/question_list.html"
	
	def get_queryset(self):
		try:
			self.category = Category.objects.get(slug__iexact=self.kwargs['slug'])
		except Category.DoesNotExist:
			raise Http404
		
		return Question.objects.get(category=self.category)