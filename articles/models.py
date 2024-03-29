from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 데이터를 위한 데이터
    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return f'{self.pk} - {self.title}'
    
