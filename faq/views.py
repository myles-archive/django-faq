from django.views.generic import ListView, DetailView

from faq.models import Question

class FAQQuestionListView(ListView):
	
	context_object_name = "question_list"
	template_name = "faq/index.html"
	
	def get_queryset(self):
		return Question.objects.all()

class FAQQuestionDetailView(DetailView):
	
	context_object_name = 'question'
	template_name = 'faq/detail.html'
	
	def get_object(self):
		return Question.objects.get(slug__iexact=self.kwargs['slug'])
