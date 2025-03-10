from django.contrib import admin

# Register your models here.
from .models import Comment, News

admin.site.register(Comment)
admin.site.register(News)

admin.site.empty_value_display = 'Не задано' 

class HomepageAdmin(admin.ModelAdmin):
    list_filter = ('news_title', 'news_publiting_date')