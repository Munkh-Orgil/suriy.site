from django.urls import path
from lesson.views import *

urlpatterns = [
    path('', LatestLessons.as_view(template_name='index.html'), name='latest_lessons'),
    path('subject/', SubjectView.as_view(template_name=''), name='subjects'),
    path('subject/<slug:slug>', SubjectDetailView.as_view(template_name='')),
    path('article/', LessonView.as_view(template_name=''), name='lessons'),
    path('article/<slug:slug>', LessonDetailView.as_view(template_name='')),
    path('test/', TestView.as_view(template_name=''), name='tests'),
    path('test/<slug:slug>', TestDetailView.as_view(template_name=''))
]   