from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from lesson.models import Subject, Article, Test, Question


class LatestArticles(ListView):
    model = Article
    context_object_name = 'articles'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest'] = Article.objects.all()[:5]
        context['subjects'] = Subject.objects.all()[:5]
        return context


class SubjectView(ListView):
    model = Subject
    context_object_name = "subjects"


class SubjectDetailView(DetailView):
    model = Subject
    context_object_name = "subject"

    def get_context_data(self, **kwargs):
        context = super(SubjectDetailView, self).get_context_data(**kwargs)
        obj = Subject.objects.get(slug=self.kwargs['slug'])
        context['articles'] = Article.objects.filter(subject=obj.pk)
        context['subjects'] = Subject.objects.all()
        print(context)
        return context


class ArticleView(ListView):
    model = Article
    template_name = 'lesson.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = Article.objects.all()
        context['subjects'] = Subject.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"

    def get_queryset(self):
        return Article.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Article.objects.get(slug=self.kwargs['slug'])
        context['test'] = Test.objects.filter(article=obj.pk)
        context['subjects'] = Subject.objects.all()
        return context 


class TestView(ListView):
    model = Test
    template_name = 'soril.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = Test.objects.filter(article=pk)
        context['subjects'] = Subject.objects.all()
        return context
    
class TestDetailView(DetailView):
    model = Test
    context_object_name = 'tests'

    def get_queryset(self):
        return Test.objects.filter(slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Test.objects.get(slug=self.kwargs['slug'])
        context['questions'] = Question.objects.filter(test=obj.pk)
        context['subjects'] = Subject.objects.all()
        return context

class QuestionView(ListView):
    model = Question
    context_object_name = 'questions'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.filter(test=pk)
        context['subjects'] = Subject.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "learnit/about-us.html"

    def context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context

class ContactView(TemplateView):
    template_name = "learnit/contact.html"

    def context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context