from django.contrib import admin

# Register your models here.
from .models import Album,Author,Genre,Song,Playlist,Country,FormatType


class SongAdmin(admin.ModelAdmin):
    search_fields = ('song_name',)
    list_filter = ('song_name',)
    
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('author_name',)
    list_filter = ('author_name',)

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ('album_name',)
    list_filter = ('album_name',)

admin.site.register(Album,AlbumAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Song, SongAdmin)
admin.site.register(Playlist)
admin.site.register(Country)
admin.site.register(FormatType)

admin.site.empty_value_display = 'Не задано'