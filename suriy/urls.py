"""suriy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from lesson.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LatestArticles.as_view(template_name='learnit/index.html'), name='latest_lessons'),
    path('subject/', SubjectView.as_view(template_name='learnit/subject.html'), name='subjects'),
    path('subject/', include('lesson.urls', namespace='lesson')),
    # path('test/', include('lesson.urls', namespace='test')),
    path('about', AboutView.as_view(), name='about-view'),
    path('contact', ContactView.as_view(), name='contact-view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
