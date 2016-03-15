from django.db import models

# Create your models here.

class Article(models.Model) :
    title = models.CharField(max_length = 100)  #������Ŀ
    category = models.CharField(max_length = 50, blank = True)  #���ͱ�ǩ
    date_time = models.DateTimeField(auto_now_add = True)  #��������
    content = models.TextField(blank = True, null = True)  #������������

    #python2ʹ��__unicode__, python3ʹ��__str__
    def __str__(self) :
        return self.title

    class Meta:  #��ʱ���½�����
        ordering = ['-date_time']