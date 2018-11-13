from django.shortcuts import render
from django.views.generic import ListView, DetailView

from lesson.models import Subject, Article, Test

class LatestLessons(ListView):
    model = Article
    context_object_name = 'lessons'

    def get_context_date(*args, **kwargs):
        context = super().get_context_date(**kwargs)
        context['latest'] = Article.objects.all[:5]
        return context

class LessonView(ListView):
    model = Article
    template_name = 'lesson.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = Article.objects.all()
        return context


class LessonDetailView(DetailView):
    model = Article


class SubjectView(ListView):
    model = Subject


class SubjectDetailView(DetailView):
    model = Subject


class TestView(ListView):
    model = Test


class TestDetailView(DetailView):
    model = Test