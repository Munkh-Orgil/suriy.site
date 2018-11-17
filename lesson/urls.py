from django.urls import path
from lesson.views import SubjectDetailView, ArticleDetailView

app_name = 'lesson'

urlpatterns = [
    path('<slug>', SubjectDetailView.as_view(
         template_name='learnit/article.html'), name="subjectDetail"),
    path('lesson/<slug>', ArticleDetailView.as_view(
         template_name='learnit/biology.html'), name="articleDetails"),
]
