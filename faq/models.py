from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

try:
	from taggit.managers import TaggableManager
except ImportError:
	TaggableManager = False

try:
	from django_markup.fields import MarkupField
except ImportError:
	MarkupField = False

class Question(models.Model):
	question = models.CharField(_('question'), max_length=200)
	answer = models.TextField(_('answer'))
	
	if MarkupField:
		markup = MarkupField(default='none')
	
	if TaggableManager:
		tags = TaggableManager(blank=True)
	
	slug = models.SlugField(_('slug'), max_length=25, unique=True)
	
	weight = models.IntegerField(_('weight'), default=0)
	
	sites = models.ManyToManyField(Site, blank=True, null=True)
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	class Meta:
		verbose_name = _('question')
		verbose_name_plural = _('questions')
		db_table = 'faq_qestions'
		get_latest_by = 'date_added'
		ordering = ('weight', '-date_added')
	
	def __unicode__(self):
		return u"%s" % self.question
	
	@permalink
	def get_absolute_url(self):
		return ('faq_question_detail', None, {
			'slug': self.slug,
		})