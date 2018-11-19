from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from lesson.models import Subject, Article, Test, Question

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """Subject model admin"""
    list_display = ['name', 'slug', 'description', 'active']
    search_fields = ['name', 'slug', 'description']
    list_filter = ['name', 'active']


@admin.register(Article)
class ArticleAdmin(AdminImageMixin, admin.ModelAdmin):
    """Article model admin"""
    list_display = ['title', 'slug', 'subject', 'class_number', 'cover', 'active']
    search_fields = ['title', 'slug', 'subject', 'class_number']
    list_filter = ['title', 'subject', 'class_number', 'active']


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    """Test model admin"""
    list_display = ['title', 'article', 'slug', 'active']
    search_fields = ['title', 'article']
    list_filter = ['title', 'article', 'active']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question model admin"""
    list_display = ['question', 'right_answer', 'answer_1', 'answer_2', 'answer_3', 'active']
    search_fields = ['question', 'right_answer', 'answer_1', 'answer_2', 'answer_3']
    list_filter = ['question', 'right_answer', 'answer_1', 'answer_2', 'answer_3', 'active']