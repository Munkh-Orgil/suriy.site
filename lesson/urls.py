from django.urls import path
from lesson.views import *

urlpatterns = [
    path('', LatestLessons.as_view(template_name='learnit/index.html'), name='latest_lessons'),
    path('subject/', SubjectView.as_view(template_name='learnit/subject.html'), name='subjects'),
    path('subject/<slug>', SubjectDetailView.as_view(template_name='learnit/article.html'), name="subjectDetail"),
    path('article/', LessonView.as_view(template_name=''), name='lessons'),
    path('article/<slug:slug>', LessonDetailView.as_view(template_name='')),
    path('test/', TestView.as_view(template_name=''), name='tests'),
    path('test/<slug:slug>', TestDetailView.as_view(template_name='')),
    path('math/', MathView.as_view(), name='math_view'),
]   