from django.contrib import admin

# Register your models here.
from .models import Comment, News

admin.site.register(Comment)
admin.site.register(News)