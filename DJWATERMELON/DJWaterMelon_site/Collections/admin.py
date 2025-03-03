from django.contrib import admin

# Register your models here.
from .models import Album,Author,Genre,Song,Playlist,Country,FormatType

admin.site.register(Album)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Country)
admin.site.register(FormatType)

