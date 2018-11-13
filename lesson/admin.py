from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from lesson.models import Subject, Article, Test

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
    list_display = ['title', 'article', 'question', 'right_answer', 'answer_1', 'answer_2', 'answer_3', 'active']
    search_fields = ['title', 'article', 'question', 'right_answer', 'answer_1', 'answer_2', 'answer_3']
    list_filter = ['title', 'article', 'question', 'right_answer', 'answer_1', 'answer_2', 'answer_3', 'active']

    