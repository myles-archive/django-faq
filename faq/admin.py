from django.contrib import admin

from faq.models import Question, Category

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

class QuestionAdmin(admin.ModelAdmin):
	list_display = (
		'question', 'weight',
	)
	prepopulated_fields = {'slug': ('question',)}
	fieldsets = (
		(None, {
			'fields': (
				('question', 'slug'),
				'answer', 'markup',
			)
		}),
		('Advanced options', {
			'classes': ('collapse',),
			'fields': (
				'tags', 'weight', 'sites',
			)
		})
	)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)