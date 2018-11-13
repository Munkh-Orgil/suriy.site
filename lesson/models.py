from django.db import models

# Create your models here.
class Lesson(models.Model):
    subject = models.CharField(max_length=50,verbose_name='Хичээлийн нэр')
    class_number = models.IntegerField(verbose_name='Ангийн тоо', null=True)
    title = models.CharField(max_length=50, verbose_name='Гарчиг', null=True)
    text = models.TextField(null=True, max_length=1000, verbose_name='Хичээлийн текст')
 
    def __str__(self):
        return "%s-%s" % (self.subject, self.title)
        

class Test(models.Model):
    question = models.CharField(max_length=100, verbose_name='Асуулт')
    title = models.CharField(max_length=50, verbose_name='Гарчиг')

    def __str__(self):
        return "Тест - %s" % (self.title)


class Answer(models.Model):
    title = models.CharField(max_length=100, verbose_name='Гарчиг')
    answer_1 = models.CharField(max_length=100, verbose_name='Асуулт-1')
    answer_2 = models.CharField(max_length=100, verbose_name='Асуулт-2')
    answer_3 = models.CharField(max_length=100, verbose_name='Асуулт-3')
    right_answer = models.CharField(max_length=100, verbose_name='Зөв хариулт')

    def __str__(self):
        return "Хариулт - %s" % (self.title)