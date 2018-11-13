import os
from django.db import models
from django.utils.text import slugify
from sorl.thumbnail import ImageField

# Create your models here.
class TimeStampedModel(models.Model):
    """TimestampedModel for easing fur  ther usage """
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(u"Төлөв", default=True)

    class Meta:
        """Meta"""
        abstract = True


class Subject(TimeStampedModel):
    name = models.CharField(u'Хичээлийн нэр', max_length=50)
    slug = models.SlugField(u"Хаяг", null=True, unique=True,
                            blank=True, allow_unicode=True)
    description = models.TextField(u"Тайлбар", null=True, blank=True)

    class Meta:
        verbose_name = u"Хичээл"
        verbose_name_plural = u"Хичээлүүд"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Subject, self).save(*args, **kwargs)


def cover_upload(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (
        instance.slug, ext
    )
    return os.path.join('article_cover/', filename)


class Article(TimeStampedModel):
    title = models.CharField(u'Гарчиг', max_length=50)
    slug = models.SlugField(u"Хаяг", null=True, unique=True,
                            blank=True, allow_unicode=True),
    class_number = models.IntegerField(verbose_name='Анги', null=True)
    body = models.TextField(u'Хичээлийн текст', blank=True)
    cover = ImageField(u"Зураг", upload_to=cover_upload)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='Subject')
 
    class Meta:
        """Meta"""
        verbose_name = u"Нийтлэл"
        verbose_name_plural = u"Нийтлэлүүд"

    def __str__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return "/{}/{}".format(Subject.slug, self.pk)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Article, self).save(*args, **kwargs)


class Test(TimeStampedModel):
    title = models.CharField(u'Гарчиг', max_length=50, blank=True, null=True)
    question = models.CharField(u'Асуулт', max_length=100, blank=True, null=True)
    answer_1 = models.CharField(u'Хариулт-1', max_length=100, blank=True, null=True)
    answer_2 = models.CharField(u'Хариулт-2', max_length=100, blank=True, null=True)
    answer_3 = models.CharField(u'Хариулт-3', max_length=100, blank=True, null=True)
    right_answer = models.CharField(u'Зөв хариулт', max_length=100, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='Article')

    class Meta:
        verbose_name = u"Сорил"
        verbose_name_plural = u"Сорилууд"

    def __str__(self):
        return "Тест - %s" % (self.title)
