from django.db import models
from django.contrib import auth
# Create your models here.
from django.conf import settings

class News(models.Model):
    news_title = models.CharField(max_length=150, verbose_name='Заголовок новости')
    news_text = models.TextField(max_length=1000, 
                                 verbose_name='Текст новости', 
                                 blank=False)
    news_publiting_date = models.DateField(verbose_name='Дата публикации', 
                                           auto_now=True)
    news_img = models.ImageField(verbose_name='Изображение новости') 
    # Добавить id пользователя-создателя новости
    news_creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новость'
        
    def __str__(self):
        self.news_title

class Comment(models.Model):
    news = models.ForeignKey(News, 
                                on_delete=models.CASCADE,
                                verbose_name='Новость', related_name='news')
    # Получить id пользователя, который оставляет комментарий
    user_comment_pk = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    comment_text = models.TextField(max_length=500, 
                                    verbose_name='Комментарий',
                                    blank=False)
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарий'
