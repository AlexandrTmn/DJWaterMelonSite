from django.db import models
from django.contrib import auth
from django.conf import settings
# Create your models here.

class Country(models.Model):
    country_name = models.CharField('Название страны', 
                                    max_length = 56, 
                                    blank=False)

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'Страна'

    def __str__(self):
        self.country_name

class Genre(models.Model):
    genre_name = models.CharField('Название жанра', 
                                  max_length = 50, 
                                  blank=False)
    #Получить id пользователя для опеределения предпочтений
    user_genre_favors = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'Жанр'

    def __str__(self):
        self.genre_name

class FormatType(models.Model):
    type_name = models.CharField('Название типа', 
                                 max_length = 20, 
                                 blank=False)

    class Meta:
        verbose_name = 'тип'
        verbose_name_plural = 'Тип'

    def __str__(self):
        self.type_name

class Song(models.Model):
    song_name = models.CharField('Название песни', 
                                 max_length = 100, 
                                 blank=False)
    song_duration = models.DurationField('Продолжительность песни', 
                                         blank=False,
                                         )
    song_release_date = models.DateField('Дата релиза',
                                         blank=True)
    song_album = models.ManyToManyField('Album')

    author = models.ManyToManyField('Author')
    county = models.ForeignKey(Country, on_delete=models.CASCADE,
                               verbose_name='Страна')
    genre = models.ForeignKey( Genre, on_delete=models.CASCADE,
                               verbose_name='Жанр')
    type = models.ForeignKey(FormatType, on_delete=models.CASCADE,
                               verbose_name= 'Тип')

    class Meta:
        verbose_name = 'песня'
        verbose_name_plural = 'Песня'

    def __str__(self):
        self.song_name

class Album(models.Model):
    album_name = models.CharField('Название альбома',
                                  max_length=100,
                                  blank=False)

    album_duration = models.DurationField('Продолжительность альбома', 
                                         blank=False,
                                         )
    album_release_date = models.DateField('Дата релиза',
                                         blank=True)
    author = models.ManyToManyField('Author')
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                               verbose_name='Страна')
    genre = models.ForeignKey( Genre, on_delete=models.CASCADE,
                               verbose_name='Жанр')
    type = models.ForeignKey(FormatType, on_delete=models.CASCADE,
                               verbose_name= 'Тип')

    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'Альбом'

    def __str__(self):
        self.album_name

class Author(models.Model):
    author_name = models.CharField('Название исполнителя(ей)',
                                   max_length=100,
                                   blank=False)
    
    author_birthday = models.DateField('Дата рождения', 
                                       blank=True)
    
    country = models.ForeignKey(Country,
                                on_delete=models.CASCADE,
                                verbose_name= 'Страна', related_name='countries')
    
    class Meta:
        verbose_name = 'исполнитель'
        verbose_name_plural = 'Исполнитель'

    def __str__(self):
        self.author_name


class Playlist(models.Model):
    playlist_name = models.CharField('Название плейлиста', 
                                     max_length=150,
                                     blank=False)
    playlist_create_date = models.DateField('Дата создания',
                                            blank=False)
    playlist_description = models.TextField('Описание плейлиста',
                                            max_length=500,
                                            blank=True)
    playlist_cover = models.ImageField(verbose_name='Изображение для плейлиста')

    song = models.ManyToManyField(Song)
    # Описать связь с текущим пользователем (создателем плейлиста)
    playlist_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'плейлист'
        verbose_name_plural = 'Плейлисты'

    def __str__(self):
        self.playlist_name
