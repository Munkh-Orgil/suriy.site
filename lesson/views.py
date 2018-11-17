from django.shortcuts import render
from django.views.generic import ListView, DetailView
from lesson.models import Subject, Article


class LatestArticles(ListView):
    model = Article
    context_object_name = 'articles'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest'] = Article.objects.all()[:5]
        context['subjects'] = Subject.objects.all()
        print(context)
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
        context['articles'] = Article.objects.filter(
             subject=obj.pk)
        print(context)
        return context


class ArticleView(ListView):
    model = Article
    template_name = 'lesson.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = Article.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"

    def get_queryset(self):
        return Article.objects.filter(slug=self.kwargs['slug'])