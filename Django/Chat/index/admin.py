from django.contrib import admin

# Register your models here.
from .models import Chat

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user_name', 'chat_data', 'chat_time')

admin.site.register(Chat, ArticleAdmin)