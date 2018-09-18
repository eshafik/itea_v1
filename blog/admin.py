from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','post_status')
    list_filter = ('post_status','created','publish','author')
    search_fields = ('title','body')
    date_hierarchy = 'publish'
