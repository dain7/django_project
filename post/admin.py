from django.contrib import admin
from .models import Post, Reply, Tag

# Register your models here.


admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Tag)
