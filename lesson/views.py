from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from lesson.models import Lesson, Test, Answer
# Create your views here.
class LatestLessons(ListView):
    model = Lesson
    context_object_name = 'lessons'

    def get_context_date(*args, **kwargs):
        context = super().get_context_date(**kwargs)
        context['latest'] = Lesson.objects.all[:5]
        return context

class LessonView(TemplateView):
    template_name = 'lesson.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = Lesson.objects.all()
        return context
