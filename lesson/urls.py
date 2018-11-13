from django.urls import path

from lesson import views
from lesson.views import LatestLessons, LessonView

urlpatterns = [
    path('index/', LatestLessons.as_view(template_name='index.html'), name='latest_lessons')
]   