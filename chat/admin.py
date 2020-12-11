from django.contrib import admin
from .models import ChatGroup

# Register your models here.
class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'mute_notifications', 'date_created', 'date_modified')
    list_filter = ('id', 'name', 'description', 'mute_notifications', 'date_created', 'date_modified')
    list_display_links = ('name',)

admin.site.register(ChatGroup, ChatGroupAdmin)
