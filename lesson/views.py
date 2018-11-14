from django.shortcuts import render
from django.views.generic import ListView, DetailView
from parler.views import TranslatableSlugMixin
from lesson.models import Subject, Article, Test

class LatestLessons(ListView):
    model = Article
    context_object_name = 'lessons'

    def get_context_date(*args, **kwargs):
        context = super(LatestLessons, self).get_context_date(**kwargs)
        context['latest'] = Article.objects.all[:5]
        context['math'] = Subject.objects.filter(subject=1)
        context['english'] = Subject.objects.filter(subject=2)
        context['physics'] = Subject.objects.filter(subject=3)        
        context['chemistry'] = Subject.objects.filter(subject=4)
        context['biology'] = Subject.objects.filter(subject=5)
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
    context_object_name = "subjects"

    def get_context_data(self, **kwargs):
        context = super(SubjectView, self).get_context_data(**kwargs)
        # context['math'] = Subject.objects.filter(subject=1)
        # context['english'] = Subject.objects.filter(subject=2)
        # context['physics'] = Subject.objects.filter(subject=3)        
        # context['chemistry'] = Subject.objects.filter(subject=4)
        # context['biology'] = Subject.objects.filter(subject=5)
        print(context)
        return context


class SubjectDetailView(TranslatableSlugMixin, DetailView):
    model = Article
    context_object_name = "articles"

    def get_context_data(self, **kwargs):
        context = super(SubjectDetailView, self).get_context_data(**kwargs)
        # context['detail'] = Subject.objects.all()
        # context['article'] = Article.objects.filter(subject=1)
        print(context)
        return context

class TestView(ListView):
    model = Test


class TestDetailView(DetailView):
    model = Test

class MathView(ListView):
    model = Article
    template_name = 'learnit/math.html'
    context_object_name = 'maths'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['math'] = Article.objects.filter(subject=1)
        context['object'] = Article.objects.all()
        return context

class EnglishView(ListView):
    model = Article
    template_name = 'learnit/english.html'
    context_object_name = 'english'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['english'] = Article.objects.filter(subject=2)
        context['object'] = Article.objects.all()
        return context

class PhysicsView(ListView):
    model = Article
    template_name = 'learnit/physics.html'
    context_object_name = 'physics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['physics'] = Article.objects.filter(subject=3)
        context['object'] = Article.objects.all()
        return context

class ChemistryView(ListView):
    model = Article
    template_name = 'learnit/chemistry.html'
    context_object_name = 'chemistry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chemistry'] = Article.objects.filter(subject=4)
        context['object'] = Article.objects.all()
        return context

class BiologyView(ListView):
    model = Article
    template_name = 'learnit/biology.html'
    context_object_name = 'biology'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biology'] = Article.objects.filter(subject=5)
        context['object'] = Article.objects.all()
        return context                